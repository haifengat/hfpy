![海风](http://git.oschina.net/uploads/2/330302_haifengat.png?1484575602)
## 海风AT
是一款开源的策略开发平台.为用户提供方便易用的策略开发工具.

## 有问题反馈
在使用中有任何问题，欢迎反馈给我，可以用以下联系方式跟我交流

- 邮件(hubert28@qq.com)
- QQ: 24918700
- Q群:65164336

## 海风AT的功能
- 策略编写
    -  提供常用指标
    -  采用HLOC调用K线数据
- 历史数据
    - <del> 提供数据日常维护服务 </del>
    - <del> 提供实时数据分钟级服务 </del>
    - <del> 提供分笔数据(内网) </del>
    - 提供历史数据库搭建服务

## 运行环境
- python 3.6
    - pyzmq
        - windows pip install pyzmq
        - linux   http://user.qzone.qq.com/24918700/blog/1507092912
    - talib
        - windows http://user.qzone.qq.com/24918700/blog/1486954718
        - linux   http://user.qzone.qq.com/24918700/blog/1483279805
    - ctp 接口
        - 下载地址 https://gitee.com/haifengat/hf_ctp_py_proxy/releases
        - 解压后,复制py_ctp到python目录下Lib/site_packages/
        - 复制dll到at上级目录,并改名为ctp_dll
## 开发环境
- vscode
    - windows  https://code.visualstudio.com/Download
    - linux  http://user.qzone.qq.com/24918700/blog/1506828997

## 发布
- git clone https://github.com/haifengat/hf_at_py.git

## 运行
- json转yaml
    - 2018.10.01配置由json改为yaml
    - [json 转 yaml](https://www.json2yaml.com/)
- 项目配置
    - config.yml
        - ctp_dll_path 指定接口dll路径
        - stra_path 策略路径[],可多个
            - 按此配置读取相应策略,按ID加载对应的参数
        - 原配置文件中的enable全部放弃(20180227)
- 策略配置
    - 与策略文件名同名的.yml文件
    - TickTest: true 分笔数据回测
    - 配置参数组
        - 必须有ID标识(int)
- 执行
    - 配置 config.yml 中的信息
    - python main.py

## 策略编写
- 策略文件名与文件内的类名要一致(区分大小写)
- 接口响应调用
    - 参见Test.py
