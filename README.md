# 以太网数据处理工具
这是一个将以太网原始数据转化为udp格式的脚本工具，用于源数据的转换，方便后期的数据分析。
Github：https://github.com/JeremyChim/Ethernet_Analysis_Tool

## 相关人员
作者：Jer小铭😎   
技术支持：Mavis🤣   
建议提供：少基同学🤪   
思路提供：家文同学😏   
测试验证：少丽同学🤨   
缺陷提出：莲花同学🤓   
开发指导：媛媛同学🤠   
技术指导：坚莲大佬🧐   
 
> 感谢各位同学和大佬的支持。^0^

## 新版本使用方法（v1.0以及更新的版本）
1. 运行.exe文件 
2. 点击浏览，选择log文件
3. 点击生成csv
4. 查看csv文件夹

## 旧版本使用方法（v0.3以及更早的版本）
1. 把日志文件命名为 log.txt 放在根目录 
2. 运行app.py 或者 app.pyw 
3. 查看csv文件夹

## 版本更新

### v1.30  
2023.6.8
- flier.py添加了容错机制，并将不满足条件的行输出在error_log.txt
- 修复了log中长度不够的行会导致卡进度条的问题，感谢坚莲大佬和莲花同学的发现🤣

### v1.26
2023.6.7
- 找当真正原因：log_17F.txt文件中长度不够的行造成的，正在构思容错机制
- 丽敏同学提出容错机制：添加判断17F信号每行的字符，如果不满足则跳过，我觉得可以

### v1.25
2023.6.6
- 坚莲大佬和莲花同学都发现了，处理某些log的时候，会出现卡在17F数据处理的情况
- 初步判断是log数据的问题
- 增加udp17F.py、udp31B.py、udp146.py的调试代码

### v1.24
2023.5.30
 - 创建一个id的脚本，看看源数据有多少个id
 - 目前可以处理17f，31b，146 这3个id的数据
 - 分析得出，源数据中还有4个数据id：232，271，5b3，5b8
 - 后续会加上那4个数据的，期待吧O(∩_∩)O

### v1.23
2023.5.30   
优化代码
- 将函数从全部导入优化为指定函数导入
- 删除一些不必要的变量
- 注释了一些暂时用不上的代码
- 修复了版本号过旧的问题😂

### v1.01
2023.5.29   
- 新增一个小功能，文件可以拖入读取路径

### v1.0
2023.5.29   
- 正式封装成exe

### v0.41
2023.5.26   
- UI新增进度条，增强体验感

### v0.4
2023.5.24
- 不过还不能用，只是有了个界面
- 把function文件夹改成func

### v0.3
2023.5.18
- 进行错误的数据进行分析，发现矩阵偏移量错误（INS_Vehicle_Lat：-90）
- 解析.C文件输出的csv，经过对比分析，发现py脚本没有错误，只是小数点后几位的差异（c语言Double类型只会保留小数点后6位，而Python则没有这个问题）
- 结论：python脚本并无错误，是矩阵和.c文件的问题
- 将udp的function脚本进行def定义，方便后期调用
- 修改config配置表的偏移量错误（INS_Vehicle_Lat：-90）

### v0.21
2023.5.17
- 少丽说有些数据是错的，暂时不知道是什么原因
- 可以自动创建cache文件夹
- 可以自动创建csv文件
- 打印进度

### v0.2
2023.5.16
- 解决了表头带引号的问题
- 直接生成csv文件，并放到csv文件夹中
- 删除没用的临时文件，和测试脚本

### v0.11
2023.5.16
- 确认可以跑了
- 删除临时编译器
- 弃用类写法，效率太慢了

### v0.1
2023.5.15
- 写了一个类，实现单个数据的转换
- 一些小改动和分类
- 添加一些测试脚本
- 更正script.py的一些错误，新建save_log.py
- 读取数据长度，切片数据的测试脚本
- 上传已完成的脚本，参考的文档
