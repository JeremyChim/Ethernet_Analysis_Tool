# 以太网数据处理工具
这是一个将以太网原始数据转化为udp格式的脚本工具，用于源数据的转换，方便后期的数据分析。

## 相关人员
作者：Jer  
技术支持：Mavis  
思路提供：家文

> 感谢Mavis和家文同学的支持。^0^

## 使用方法
1. 把日志文件命名为 log.txt 放在根目录 
2. 运行app.py  
3. 查看csv文件夹

## 版本更新
## v0.21
- 少丽说有些数据是错的，暂时不知道是什么原因
- 可以自动创建cache文件夹
- 可以自动创建csv文件
- 打印进度

### v0.2
- 解决了表头带引号的问题
- 直接生成csv文件，并放到csv文件夹中
- 删除没用的临时文件，和测试脚本

### v0.11
- 确认可以跑了
- 删除临时编译器
- 弃用类写法，效率太慢了

### v0.1
- 写了一个类，实现单个数据的转换
- 一些小改动和分类
- 添加一些测试脚本
- 更正script.py的一些错误，新建save_log.py
- 读取数据长度，切片数据的测试脚本
- 上传已完成的脚本，参考的文档