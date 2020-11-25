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

### talab 指标库
  [https://www.ta-lib.org/function.html](https://www.ta-lib.org/function.html)

## docker运行
### docker-compose.yml
```yaml
version: "3.7"

services:
    hfpy:
        image: hfpy:1104
        container_name: hfpy
        restart: always
        environment:
            # 策略信号入库使用
            - pg_config=postgresql://postgres:12345@hfpy_pg:5432/postgres
        volumes: 
            # 个人策略文件夹
            - ./strategies:/hfpy/strategies
            # hfpy配置
            - ./config:/hfpy/config
        depends_on:
            - hfpy_pg
   hfpy_pg:
        image: postgres:12-alpine
        container_name: hf_pg
        restart: always
        environment:
            - TZ=Asia/Shanghai
            - POSTGRES_PASSWORD=12345
        ports:
            - "25432:5432"
        volumes:
            - ./pg_data:/var/lib/postgresql/data
        
# docker pull haifengat/hfpy && docker tag haifengat/hfpy haifengat/hfpy:`date '+%m%d'` && docker push haifengat/hfpy:`date '+%m%d'`
```
### 运行
```bash
docker-compose up -d
```
### 配置docker-compose.yml
#### 环境变量
* pg_min
    * postgresql://postgres:123456@hf_pg:5432/postgres?sslmode=disable
    * 分钟数据库
* pg_order
    * postgresql://postgres:123456@pg_order:5432/postgres?sslmode=disable
    * 策略信号数据库
* redis_addr
    * ip:port
    * 实时分钟数据库 [md.{instrument}]
    * 实时order [order.{stra_name}.{stra_id}]
* app
    * 信号入库为color模式
* single_order_one_bar
    * 是否K线只发一个委托,默认 True
#### Volume
* /hfpy/strategy 策略路径
* /hfpy/config 配置文件路径
## 策略信号入库
```python
# 修改 strategy.py 顶部增加
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
import os, time

# 在策略的 __init__(self) 中增加
        ########### 信号入库 ########################
        if 'pg_config' in os.environ: # 环境变量作为开关
            pg_config = os.environ['pg_config']
            self.pg:Engine = create_engine(pg_config)        
            print(f'connecting pg: {pg_config}')
            # 清除策略信号
            self.pg.execute(f"DELETE FROM public.strategy_sign WHERE strategy_id='{self.ID}'")

# 修改 __OnOrder
    def __OnOrder(self, data: Data, order: OrderItem):
        """调用外部接口的reqorder"""
        # 同时接口发单可不注释 
        # self._data_order(self, data, order)
        if 'pg_config' in os.environ: # 环境变量作为开关
            color = 'red' if order.Direction == DirectType.Buy else 'green'
            sign = f'{{"color": {color}, "price": {order.Price}}}'
            sql = f"""INSERT INTO public.strategy_sign
    (tradingday, order_time, instrument, "period", strategy_id, sign, remark, insert_time)
    VALUES('{time.strftime('%Y%m%d', time.localtime())}', '{self.D[-1]}', '{self.Instrument}', {self.Interval}, '{self.ID}', '{sign}', '', now())"""
            self.pg.execute(sql)
```

## 本地部署
### hfpy 安装
`pip install hfpy`

### 使用
- 安装python组件 `pip install -r requirements.txt`
- 新建目录
- 创建main.py并复制粘贴下面示例中main的内容
- 创建strategies子目录
- 在strategies目录下,创建SMACross.py和SMACross.yml文件【注意大小写】,并复制粘贴示例中对应的代码.
- 执行 python main.py 

## 测试报告
因报告使用了pandas所以被注释掉了，如需要则可以自行安装pandas并注释掉atp.py的5行和252行。

## 配置说明
- 项目配置 config.yml
  - 当前工作目录下无此文件时, 会产生默认配置
  - stra_path 策略路径[],可多个
    - 按此配置读取相应策略,按ID加载对应的参数
- 策略配置
  - 与策略文件名同名的.yml文件
  - 配置参数组
    - 必须有ID标识(int)
  - TickTest: true
    - 分笔数据回测,需处理数据源及格式
- 执行
  - 配置 config.yml 中的登录信息，数据源
  - python main.py

### 策略编写

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
from time import sleep

if __name__ == '__main__':
    ATP().Run()
    while True:
        sleep(60*10)
```

#### config.yml
```yaml
---
ctp_config:
    # 为空时不登录接口
    ctp_front: 'sim_now'
    investor: '008107'
    password: '1'
    product_info: ''
    app_id: 'simnow_client_test'
    auth_code: '0000000000000000'
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
# 数据源 - zmq配置
zmq_config: tcp://私有化部署数据服务:15555
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
__mtime__ = '2016/8/16'
"""
# import talib._ta_lib as talib
from hfpy.data import Data
from hfpy.bar import Bar
from hfpy.strategy import Strategy
import numpy as np
import talib as ta

class SMACross(Strategy):

    def __init__(self, jsonfile):
        super().__init__(jsonfile)
        self.p_ma1 = self.Params['MA1']
        self.p_ma2 = self.Params['MA2']
        self.p_lots = self.Params['Lots']

    def OnBarUpdate(self, data=Data, bar=Bar):
        if len(self.C) < self.p_ma2:
            return
        # if len(data.Instrument) > 0:
        #     print(f'{data.Tick.Instrument},{data.Tick.Volume}')

        # print('{0}-{1}'.format(self.D[-1], self.C[-1]))
        ma1 = ta.SMA(np.array(self.C, dtype=float), self.p_ma1)
        ma2 = ta.SMA(np.array(self.C, dtype=float), self.p_ma2)

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
        Instrument: p2105
        IntervalType: Minute
        Interval: 5
    -
        Instrument: rb2105
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
        Instrument: rb2105
        IntervalType: Minute
        Interval: 5
    Params:
        Lots: 1
        MA1: 5
        MA2: 60
```
