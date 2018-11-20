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

### python >3.6

- anaconda
    - 下载安装 [https://www.anaconda.com/download](https://www.anaconda.com/download)

- talib
  - windows [http://user.qzone.qq.com/24918700/blog/1486954718](http://user.qzone.qq.com/24918700/blog/1486954718)
  - linux [http://user.qzone.qq.com/24918700/blog/1483279805](http://user.qzone.qq.com/24918700/blog/1483279805)

### ctp 接口
- `pip install py_ctp`
- <del>下载 [https://gitee.com/haifengat/hf_ctp_py_proxy/releases](https://gitee.com/haifengat/hf_ctp_py_proxy/releases)</del>
- <del>解压后,复制py_ctp到python目录下Lib/site_packages/</del>
- <del>复制dll到at上级目录,并改名为ctp_dll</del>


## 开发环境

- vscode
  - windows [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
  - linux   [http://user.qzone.qq.com/24918700/blog/1506828997](http://user.qzone.qq.com/24918700/blog/1506828997)
- pycharm
    - http://www.jetbrains.com/pycharm/download/index.html
 
## 发布

```bash
国内 https://gitee.com/haifengat/at_py
国际 https://github.com/haifengat/hf_at_py
```

## 运行

- json转yaml
  - 2018.10.01配置由json改为yaml
  - [json 转 yaml](https://www.json2yaml.com/)
- 项目配置 config.yml
  - 当前工作目录下无此文件时会复制原始配置到此目录下
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

