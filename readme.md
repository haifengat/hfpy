![海风](http://git.oschina.net/uploads/2/330302_haifengat.png?1484575602)
## 海风AT
是一款开源的策略开发平台.为用户提供方便易用的策略开发工具.

## 有问题反馈
在使用中有任何问题，欢迎反馈给我，可以用以下联系方式跟我交流

* 邮件(hubert28@qq.com)
* QQ: 24918700
* Q群:65164336
* 代码同步
    * https://github.com/haifengat
## 海风AT的功能
* 策略编写
    *  提供常用指标
    *  采用HLOC调用K线数据
* 历史数据
    *  提供数据日常维护服务
    *  提供实时数据分钟级服务
    *  提供分笔数据(内网)
## 运行环境
* python 3.6
    * pyzmq
        * windows pip install pyzmq
        * linux   http://user.qzone.qq.com/24918700/blog/1507092912
    * talib
        * windows http://user.qzone.qq.com/24918700/blog/1486954718
        * linux   http://user.qzone.qq.com/24918700/blog/1483279805
## 开发环境
* vscode
    * windows  https://code.visualstudio.com/Download
    * linux  http://user.qzone.qq.com/24918700/blog/1506828997
## 发布
* git clone https://github.com/haifengat/hf_at_py.git
## 运行
* 项目配置
    * stra_test.json
        * stra_path 策略路径[],可多个
* 策略配置
    * 与策略文件名同名的.json文件
        * 
* 调用目录下创建log目录
* 执行 python py_at/stra_test.py ivnestor pwd (*不要加引号*)
## 策略编写
* 策略文件名与文件内的类名要一致(区分大小写)
* 接口响应调用
    * 参见Test.py
## 策略配置
* 策略同级目录下的配置文件命名规则: 策略名_xxx
    * 如策略名ABC, 配置文件可用ABC_01 ABC_02 ...
    * 若同级目录下没有配置文件,则寻找"策略名.json"的配置文件
    * 若还未找到,则加载失败
* 同一策略可以配置多套参数
* 不在同级目录下,或命名不符规划的配置不被加载
## 附atom快捷键
  * ctrl+t 查找文件
  * ctrl+b 打开的文件之间切换
  * ctrl+r 在方法爱之间跳转
  * alt+ctrl+[ 折叠
  * alt+ctrl+] 展开
  * alt+ctrl+shift+[ 折叠全部
  * alt+ctrl+shift+] 展开全部
  
