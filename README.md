# 一键日工具集
# 下载和使用
~~~
git clone https://github.com/codervibe/OneKeyClickFuckToolkit.git
cd OneKeyClickFuckToolkit
python .\main\oneKeyClickToolkit.py
~~~
# 一键日卫星
* 启动脚本 输入```1``` 即可启动

# 一键日服务器
启动脚本 输入```2``` 即可启动
* 还未开发完成
# 一键日wifi
* 启动脚本 输入```3``` 即可启动
* 需要外接无线网卡 否则会断掉自带的无线网卡的网络（主板上的）
* 一键日 wifi 已经适配 Linux 不过需要 kali linux 能够识别出来的网卡 比如 
* Realtek RTL8811AU Wireless LAN 802.11ac USB 2.0 Network Adapter
# 破解wifi握手包
* 使用脚本破解抓好的握手包
* 启动脚本 输入```4``` 即可启动 （暂时这样还没想好）
# 一键CMS指纹识别
*  启动脚本 输入```5``` 即可启动
## 运行效果
~~~text
请选择一个操作:
1. 一键日卫星
2. 一键日服务器
3. 一键破解wifi
4. 破解wifi握手包
5. 一键CMS指纹识别
0. 退出
PS>1
扫描当前可用的地址...
|██████████████████████████████████████████████████| 100.0% 扫描地址
找到可用地址, 按回车键显示地址列表，或等待 3 秒自动继续。
自动选择可用的卫星...
|██████████████████████████████████████████████████| 100.0% 选择卫星
已选择卫星地址: 192.168.1.65
正在尝试生成字典...
|██████████████████████████████████████████████████| 100.0% 生成字典
正在尝试破解控制系统密码...
|██████████████████████████████████████████████████| 100.0% 破解控制系统密码
正在尝试破解控制系统...
|██████████████████████████████████████████████████| 100.0% 破解控制系统
操作完成!
请选择一个操作:
1. 一键日卫星
2. 一键日服务器
3. 一键破解wifi
4. 破解wifi握手包
5. 一键CMS指纹识别
0. 退出
PS>2
请输入要扫描的主机地址 (例如，127.0.0.1): 127.0.0.1
请输入要扫描的端口 (逗号分隔或 'all' 表示所有端口): all
正在扫描 127.0.0.1 上的指定端口...

扫描端口:   0%|                                                                                                                       | 8/65535 [00:09<20:36:11,  1.13s/port] 

程序被中断.

请选择一个操作:
1. 一键日卫星
2. 一键日服务器
3. 一键破解wifi
4. 破解wifi握手包
5. 一键CMS指纹识别
0. 退出
PS>2
正在执行一键日服务器...
请输入要扫描的主机地址 (例如，127.0.0.1): 127.0.0.1
请输入要扫描的端口 (逗号分隔或 'all' 表示所有端口): 80,8080,3306,6379 
正在扫描 127.0.0.1 上的指定端口...

扫描端口: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.01s/port]
未找到开放端口。
|██████████████████████████████████████████████████| 100.0% 获取真实IP
|██████████████████████████████████████████████████| 100.0% 扫描服务器C段
|██████████████████████████████████████████████████| 100.0% 子域名信息收集
一键日服务器完成!
~~~
# 本来 是 有实用功能 但是由于 这样会有没有目的性 情况所以 修改代码将实用性的部分 重新 创建出一个新的项目 
* 项目地址
~~~
https://github.com/codervibe/VibePracticalToolkitSet.git
~~~
# 声明 
* 本项目只做技术交流 使用本项目造成的违法行为 与本人无关 
* 切勿用于任何违法用途