#

![海风](http://git.oschina.net/uploads/2/330302_haifengat.png?1484575602)

## 海风py

一款开源的策略开发平台.为用户提供方便易用的策略开发工具.

## 有问题反馈

在使用中有任何问题，欢迎反馈给我，可以用以下联系方式跟我交流

- 邮件(hubert28@qq.com)
- QQ: 24918700
- Q群:65164336

## 海风AT的功能

- 策略编写
  - 提供常用指标
  - 采用HLOC调用K线数据
- 历史数据
  - 提供每日数据
  - 提供实时数据分钟级服务
  - <del> 提供分笔数据(内网) </del>

## 运行环境

### tulipy 指标库
  [https://tulipindicators.org/](https://tulipindicators.org/)

### hfpy 安装
`pip install hfpy`

### docker
`docker pull haifengat/hfpy`
```yaml
version: "3.7"

services:
    hfpy:
        image: haifengat/hfpy
        container_name: hfpy
        restart: always
        ports: 
            - "2222:22"
        environment:
            # config.yml所在目录
            config_path: /home/
        volumes: 
            # 个人策略文件夹
            - ./strategies:/home/strategies
```

### 使用
- 安装python组件 `pip install -r requirements.txt`
- 新建目录
- 创建main.py并复制粘贴下面示例中main的内容
- 创建strategies子目录
- 在strategies目录下,创建SMACross.py和SMACross.yml文件【注意大小写】,并复制粘贴示例中对应的代码.
- 执行 python main.py 


## 开发工具

- vscode
  - windows [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
  - linux   [http://user.qzone.qq.com/24918700/blog/1506828997](http://user.qzone.qq.com/24918700/blog/1506828997)
- pycharm
    - http://www.jetbrains.com/pycharm/download/index.html
 

## 配置说明

- json转yaml
  - 2018.10.01配置由json改为yaml
  - [json 转 yaml](https://www.json2yaml.com/)
- 项目配置 config.yml
  - 当前工作目录下无此文件时, 首次运行会复制原始配置到此目录下
  - <del>ctp_dll_path 指定接口dll路径</del>
  - stra_path 策略路径[],可多个
    - 按此配置读取相应策略,按ID加载对应的参数
    - 原配置文件中的enable全部放弃(20180227)
- 策略配置
  - 与策略文件名同名的.yml文件
  - 配置参数组
    - 必须有ID标识(int)
  - TickTest: true
    - 分笔数据回测,需处理数据源及格式
- 执行
  - 配置 config.yml 中的信息
  - python main.py

## 策略编写

- 策略文件名与文件内的类名要一致(区分大小写)
- 示例
    - strategies/SMACross.py
    - strategies/Test.py
        - 接口调用示例

### 示例

#### main.py
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '主程序'
__author__ = 'HaiFeng'
__mtime__ = '20180822'

from hfpy.atp import ATP

if __name__ == '__main__':
    ATP().Run()
    while input().lower() != 'q':
        continue
```

#### config.yml
```yaml
---
ctp_config:
    # 为空时不登录
    ctp_front: ''
    investor: '008105'
    password: '1'
    product_info: ''
    app_id: ''
    auth_code: ''
    # 追单设置
    chasing:
        # n秒后不成交则撤单重发[0-不追单]
        wait_seconds: 3
        # 超价重发n个pricetick
        offset_ticks: 2
        # 重发次数,n次重发后仍未成交则[板价发单]
        resend_times: 3
    # ctp前置配置
    fronts:
        sim_now:
            trade: tcp://180.168.146.187:10000
            quote: tcp://180.168.146.187:10010
            broker: '9999'
        ebf:
            trade: tcp://192.168.52.4:41205
            quote: tcp://192.168.52.4:41213
            broker: '6000'
# 数据源 - zmq配置
zmq_config: tcp://broadcast.eicp.net:55881
# 开关
onoff:
    # 是否7*24
    running_as_server: true
    # 是否发送委托
    real_order_enable: false
    # 一根K线只发送一次指令
    single_order_one_bar: true
    # 是否打印行情时间
    show_tick_time: true
# 策略路径配置
stra_path:
    # 路径
    strategies:
        # 策略文件名
        SMACross:
        # 策略配置参数ID
        - 119
```

#### SMACross.py
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2020/07/30'
"""

# import talib._ta_lib as talib
from hfpy.data import Data
from hfpy.bar import Bar
from hfpy.strategy import Strategy
import numpy as np
import tulipy as ti

class SMACross(Strategy):

    def __init__(self, jsonfile):
        super().__init__(jsonfile)
        self.p_ma1 = self.Params['MA1']
        self.p_ma2 = self.Params['MA2']
        self.p_lots = self.Params['Lots']

    def OnBarUpdate(self, data=Data, bar=Bar):
        if len(self.C) < self.p_ma2:
            return
        print(f'macross: {data.D[-1]}')
        # if len(data.Instrument) > 0:
        #     print(f'{data.Tick.Instrument},{data.Tick.Volume}')

        # print('{0}-{1}'.format(self.D[-1], self.C[-1]))
        ma1 = ti.sma(np.array(self.C, dtype=float), self.p_ma1)
        ma2 = ti.sma(np.array(self.C, dtype=float), self.p_ma2)

        self.IndexDict['ma5'] = ma1
        self.IndexDict['ma10'] = ma2

        if len(ma2) < 2 or len(ma1) < 2:
            return
        if self.PositionLong == 0:
            if ma1[-1] >= ma2[-1] and ma1[-2] < ma2[-2]:
                if self.PositionShort > 0:
                    self.BuyToCover(self.O[-1], self.p_lots, '买平')
                self.Buy(self.O[-1], self.p_lots, '买开')
        elif self.PositionShort == 0:
            if ma1[-1] <= ma2[-1] and ma1[-2] > ma2[-2]:
                if self.PositionLong > 0:
                    self.Sell(self.O[-1], self.p_lots, '卖平')
                self.SellShort(self.O[-1], self.p_lots, '卖开')
```

#### SMACross.yml

```yaml
---
# ID用于区分不同策略实例的委托
- 
    ID: 119
    BeginDate: 20191101
    TickTest: false
    # 可通过增加Data实现多合约多周期引用
    Datas:
    -
        Instrument: p2001
        IntervalType: Minute
        Interval: 5
    -
        Instrument: rb2009
        IntervalType: Minute
        Interval: 5
    Params:
        Lots: 1
        MA1: 10
        MA2: 20
- 
    ID: 120
    BeginDate: 20180901
    Datas:
    - 
        Instrument: rb1910
        IntervalType: Minute
        Interval: 5
    Params:
        Lots: 1
        MA1: 5
        MA2: 60
```
