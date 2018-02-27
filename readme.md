![海风](http://git.oschina.net/uploads/2/330302_haifengat.png?1484575602)
## 海风AT
是一款开源的策略开发平台.为用户提供方便易用的策略开发工具.

## 有问题反馈
在使用中有任何问题，欢迎反馈给我，可以用以下联系方式跟我交流

- 邮件(hubert28@qq.com)
- QQ: 24918700
- Q群:65164336
- 代码同步
    - https://github.com/haifengat

## 海风AT的功能
- 策略编写
    -  提供常用指标
    -  采用HLOC调用K线数据
- 历史数据
    -  提供数据日常维护服务
    -  提供实时数据分钟级服务
    -  提供分笔数据(内网)

## 运行环境
- python 3.6
    - pyzmq
        - windows pip install pyzmq
        - linux   http://user.qzone.qq.com/24918700/blog/1507092912
    - talib
        - windows http://user.qzone.qq.com/24918700/blog/1486954718
        - linux   http://user.qzone.qq.com/24918700/blog/1483279805

## 开发环境
- vscode
    - windows  https://code.visualstudio.com/Download
    - linux  http://user.qzone.qq.com/24918700/blog/1506828997

## 发布
- git clone https://github.com/haifengat/hf_at_py.git

## 运行
- 项目配置
    - stra_test.json
        - stra_path 策略路径[],可多个
            - path:{file:[ID]}
            - 目录,文件(不带py),策略配置中参数的ID
            - 按此配置读取相应策略,按ID加载对应的参数
        - 原配置文件中的enable全部放弃(20180227)
- 策略配置
    - 与策略文件名同名的.json文件
    - 配置参数组
        - 必须有ID标识(int)
- 执行
    - python py_at/stra_test.py ivnestor pwd (*不要加引号*)
    - 或配置stra_test.json中的信息

## 策略编写
- 策略文件名与文件内的类名要一致(区分大小写)
- 接口响应调用
    - 参见Test.py

## 策略配置
- 策略同级目录下的配置文件命名规则: 策略名_xxx
    - 如策略名ABC, 配置文件可用ABC_01 ABC_02 ...
    - 若同级目录下没有配置文件,则寻找"策略名.json"的配置文件
    - 若还未找到,则加载失败
- 同一策略可以配置多套参数
- 不在同级目录下,或命名不符规划的配置不被加载

## 附vscode快捷键
###主命令框
- F1 或 Ctrl+Shift+P: 打开命令面板。在打开的输入框内，可以输入任何命令，例如：
    - 按一下 Backspace 会进入到 Ctrl+P 模式
    - 在 Ctrl+P 下输入 > 可以进入 Ctrl+Shift+P 模式

- 在 Ctrl+P 窗口下还可以:
    - 直接输入文件名，跳转到文件
    - ? 列出当前可执行的动作
    - ! 显示 Errors或 Warnings，也可以 Ctrl+Shift+M
    - : 跳转到行数，也可以 Ctrl+G 直接进入
    - @ 跳转到 symbol（搜索变量或者函数），也可以 Ctrl+Shift+O 直接进入
    - @ 根据分类跳转 symbol，查找属性或函数，也可以 Ctrl+Shift+O 后输入:进入
    - '#根据名字查找 symbol，也可以 Ctrl+T

### 常用快捷键
- 编辑器与窗口管理
    - 打开一个新窗口： Ctrl+Shift+N
    - 关闭窗口： Ctrl+Shift+W
    - 同时打开多个编辑器（查看多个文件）
    - 新建文件 Ctrl+N
    - 文件之间切换 Ctrl+Tab
    - 切出一个新的编辑器（最多 3 个） Ctrl+\，也可以按住 Ctrl 鼠标点击 Explorer 里的文件名
    - 左中右 3 个编辑器的快捷键 Ctrl+1 Ctrl+2 Ctrl+3
    - 3 个编辑器之间循环切换 Ctrl+
    - 编辑器换位置， Ctrl+k然后按 Left或 Right

### 代码编辑
- 格式调整
    - 代码行缩进 Ctrl+[ 、 Ctrl+]
    - Ctrl+C 、 Ctrl+V 复制或剪切当前行/当前选中内容
    - 代码格式化： Shift+Alt+F，或 Ctrl+Shift+P 后输入 format code
    - 上下移动一行： Alt+Up 或 Alt+Down
    - 向上向下复制一行： Shift+Alt+Up 或 Shift+Alt+Down
    - 在当前行下边插入一行 Ctrl+Enter
    - 在当前行上方插入一行 Ctrl+Shift+Enter
- 光标相关
    - 移动到行首： Home
    - 移动到行尾： End
    - 移动到文件结尾： Ctrl+End
    - 移动到文件开头： Ctrl+Home
    - 移动到定义处： F12
    - 定义处缩略图：只看一眼而不跳转过去 Alt+F12
    - 移动到后半个括号： Ctrl+Shift+]
    - 选择从光标到行尾： Shift+End
    - 选择从行首到光标处： Shift+Home
    - 删除光标右侧的所有字： Ctrl+Delete
    - 扩展/缩小选取范围： Shift+Alt+Left 和 Shift+Alt+Right
    - 多行编辑(列编辑)：Alt+Shift+鼠标左键，Ctrl+Alt+Down/Up
    - 同时选中所有匹配： Ctrl+Shift+L
    - Ctrl+D 下一个匹配的也被选中 (在 sublime 中是删除当前行，后面自定义快键键中，设置与 Ctrl+Shift+K 互换了)
    - 回退上一个光标操作： Ctrl+U
- 重构代码
    - 找到所有的引用： Shift+F12
    - 同时修改本文件中所有匹配的： Ctrl+F12
    - 重命名：比如要修改一个方法名，可以选中后按 F2，输入新的名字，回车，会发现所有的文件都修改了
    - 跳转到下一个 Error 或 Warning：当有多个错误时可以按 F8 逐个跳转
    - 查看 diff： 在 explorer 里选择文件右键 Set file to compare，然后需要对比的文件上右键选择 Compare with file_name_you_chose
- 查找替换
    - 查找 Ctrl+F
    - 查找替换 Ctrl+H
    - 整个文件夹中查找 Ctrl+Shift+F
- 显示相关
    - 全屏：F11
    - zoomIn/zoomOut：Ctrl +/-
    - 侧边栏显/隐：Ctrl+B
    - 显示资源管理器 Ctrl+Shift+E
    - 显示搜索 Ctrl+Shift+F
    - 显示 Git Ctrl+Shift+G
    - 显示 Debug Ctrl+Shift+D
    - 显示 Output Ctrl+Shift+U
  
