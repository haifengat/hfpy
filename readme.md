#

![海风](http://git.oschina.net/uploads/2/330302_haifengat.png?1484575602)

## HFpy

一款开源的策略开发平台.为用户提供方便易用的策略开发工具.

## 海风AT的功能

- 策略编写
  - 提供常用指标
  - 采用HLOC调用K线数据
- 历史数据
  - 提供每日数据
  - 提供实时数据分钟级服务

## 运行环境

### talab 指标库
  [https://www.ta-lib.org/function.html](https://www.ta-lib.org/function.html)

### 生成镜像
```bash
docker build -t haifengat/hfpy:`date +%Y%m%d` .
# hub.docker.com
docker push haifengat/hfpy:`date +%Y%m%d`
```

### 配置docker-compose.yml
#### 环境变量
* strategy_names
  * 策略名列表，用","分隔
  * 对应的strategies目录下同名策略文件
* single_order_one_bar
    * 是否K线只发一个委托,默认 True
* pg_min
    * postgresql://postgres:123456@hf_pg:5432/postgres?sslmode=disable
    * 分钟数据库
* pg_order
    * postgresql://postgres:123456@pg_order:5432/postgres?sslmode=disable
    * 策略信号数据库
* redis_addr
    * ip:port
    * 实时分钟数据库 [md.{instrument}] 读取
    * 实时order [order.{stra_name}.{stra_id}] 写入

### 示例 docker-compose.yml
```yaml
version: "3.7"

services:
    hf_py:
        image: haifengat/hfpy
        container_name: hf_py
        restart: always
        environment:
            - TZ=Asia/Shanghai
            - strategy_names="SMACross"
            # 当日分钟与实时分钟
            - redis_addr="172.19.129.98:16379"
            # 分钟数据,没配置zmq时使用
            - pg_min=postgresql://postgres:12345@hf_py_pg:5432/postgres
            # 策略信号入库使用
            - pg_order=postgresql://postgres:12345@hf_py_pg:5432/postgres
        volumes:
            # 个人策略文件夹
            - ./strategies:/hfpy/strategies
```

## 策略信号
### 策略生成的信号会插件到postgres的public.strategy_sign中
```python
js = json.dumps({
                    'Direction': str(order.Direction).split('.')[1],
                    'Offset': str(order.Offset).split('.')[1],
                    'Price': round(order.Price, 4),
                    'Volume': order.Volume
                })
sql = f"""INSERT INTO public.strategy_sign
(tradingday, order_time, instrument, "period", strategy_id, strategy_group, sign, remark, insert_time)
VALUES('{data.Bars[-1].Tradingday}', '{stra.D[-1]}', '{data.Instrument}', {data.Interval}, '{stra.ID}', '{type(stra).__name__}', '{js}', '', now())"""
```
### 实时信号会发布到redis
```python
js = json.dumps({
                'Instrument': order.Instrument,
                'Direction': str(order.Direction).split('.')[1],
                'Offset': str(order.Offset).split('.')[1],
                'Price': round(order.Price, 4),
                'Volume': order.Volume,
                "ID": stra.ID * 1000 + len(stra.Orders) + 1
                })
self.cfg.rds.publish(f'order.{type(stra).__name__}', js)
```

## 测试报告
因报告使用了pandas所以被注释掉了，如需要则可以自行安装pandas并注释掉atp.py的5行和252行。

## 策略配置
  - 与策略文件名同名的.yml文件
  - 配置参数组
    - 必须有ID标识(int)
```yml
---
-
    # ID用于区分不同策略实例的委托不可重复
    "ID": 901
    # 回测开始日期
    "BeginDate": 20200101
    # 可通过增加Data实现多合约多周期引用
    "Datas": 
    -
        # 合约/周期/周期数
        "Instrument": "ag2012"
        "IntervalType": "Minute"
        "Interval": 5
    "Params": 
        # 突破轨道的长度
        "LENGTH1": 46
        "OPENPARAM": 0.54
```

### 策略编写

**策略文件名与类名、配置文件名要一致(区分大小写)**

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

## 附
### talib安装
报错：#include "Python.h
解决：
 apt: apt-get install python3-dev
 yum: yum install python3-devel
