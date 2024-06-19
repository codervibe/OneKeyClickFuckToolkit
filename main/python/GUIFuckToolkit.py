import time
import tkinter as tk
from tkinter import ttk
from rich import progress_bar
from util.simulateprogressbar import simulate_progress_bar
from onekeyclickfucksatellite import onekeyclickfucksatellite
from onekeyclickfuckserver import informationcollection


def 一键日服务器():
    """
    执行一键日服务器.
    """
    try:
        print("正在执行一键日服务器...")
        informationcollection()
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键日卫星():
    print("正在执行一键日卫星...")
    try:
        onekeyclickfucksatellite()
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键顺着网线砍人():
    try:
        print("正在执行一键顺着网线砍人...")
        simulate_progress_bar("一键顺着网线砍人", 80)
        print("\033[92m一键顺着网线砍人完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键给对手戴绿帽():
    try:
        simulate_progress_bar("一键给对手戴绿帽", 80)
        print("\033[92m你已经送给对手一顶大绿帽\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键召唤陨石砸向对手():
    try:
        print("正在执行一键召唤陨石砸向对手...")
        simulate_progress_bar("正在念动咒语", 80)
        simulate_progress_bar("召唤陨石砸向对手", 60)
        print("\033[92m一键召唤陨石砸向对手完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键拔掉对方网线():
    try:
        simulate_progress_bar("一键拔掉对方网线", 80)
        print("\033[92m对方网线已经被切断\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键盗QQ号():
    try:
        simulate_progress_bar("正在给对方传播木马", 80)
        simulate_progress_bar("正在等待对方上钩", 60)
        simulate_progress_bar("对方已上钩 正在盗取", 60)
        print("\033[92mQQ号现在是我们的了 任务完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键日进内网():
    try:
        simulate_progress_bar("正在搜索对方内网漏洞", 90)
        simulate_progress_bar("已找到对方漏洞正在尝试利用", 60)
        simulate_progress_bar("正在释放病毒", 60)
        simulate_progress_bar("正在提权", 60)
        print("\033[92m成功 现在对方内网是我们的了!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键挖洞():
    try:
        simulate_progress_bar("正在寻找漏洞", 60)
        print("\033[92m任务完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键刷Q币():
    try:
        simulate_progress_bar("一键刷Q币", 160)
        print("\033[92m完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键挖比特币():
    try:
        simulate_progress_bar("一键挖比特币", 160)
        print("\033[92m一键挖比特币完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键刷会员():
    try:
        simulate_progress_bar("一键刷会员", 160)
        print("\033[92m一键刷会员完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键日教务系统():
    try:
        print("正在执行一键日教务系统...")
        simulate_progress_bar("正在查找教务系统漏洞", 60)
        simulate_progress_bar("正在尝试弱密码爆破", 60)
        print("\033[92m密码已找到!\033[0m\n")
        simulate_progress_bar("正在尝试登录", 60)
        print("\033[92m登陆完成.......!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键社工管理员全家():
    try:
        print("正在执行一键社工管理员全家")
        simulate_progress_bar("正在查找管理员个人信息", 260)
        simulate_progress_bar("正在查找管理员全家信息", 160)
        print("\033[92m信息已找到 任务完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键DDOS():
    try:
        simulate_progress_bar("正在发动DDOS 攻击", 160)
        simulate_progress_bar("正在模拟正常用户访问", 160)
        print("\033[92m对方服务器已经未响应!\033[0m\n")
        print("\033[92m任务完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键让对方拉稀():
    try:
        simulate_progress_bar("正在监听对方外卖地址", 89)
        simulate_progress_bar("正在监听拦截外卖小哥", 89)
        simulate_progress_bar("正在给外卖下药", 89)
        simulate_progress_bar("正在将外卖正常送达", 89)
        print("\033[92m对方已经拉稀!\033[0m\n")
        print("\033[92m任务完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def 一键支付宝充值100万():
    try:
        simulate_progress_bar("正在破解支付宝系统", 89)
        simulate_progress_bar("正在绕过防火墙", 289)
        simulate_progress_bar("正在破解防护系统", 489)
        simulate_progress_bar("正在反击", 689)
        simulate_progress_bar("正在隐藏自己的位置", 189)
        simulate_progress_bar("正在破解密码", 489)
        simulate_progress_bar("正在尝试修改钱包余额", 49)
        print("\033[92m修改成功!\033[0m\n")
        simulate_progress_bar("正在删除操作日志", 189)
        simulate_progress_bar("正在删除代理服务器操作日志", 189)
        print("\033[92m任务完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def print_banner():
    banner = r"""
 _       __     __                              __    
| |     / /__  / /________  ____ ___  ___  ____/ /____
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \/ __  / ___/
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/ /_/ (__  ) 
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/\__,_/____/  
        """
    print(banner)


def create_gui():
    """
    创建图形界面.
    """
    root = tk.Tk()
    root.title("黑客工具箱")

    frame = ttk.Frame(root, padding="10")
    frame.grid()

    # 创建一个标签显示程序标题
    label_title = ttk.Label(frame, text="黑客工具箱", font=("Helvetica", 16))
    label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # 添加一个按钮用于选择每个操作
    ttk.Button(frame, text="一键日卫星", command=lambda: 一键日卫星()).grid(row=1,
                                                                            column=0,
                                                                            sticky="ew",
                                                                            padx=5,
                                                                            pady=5)
    ttk.Button(frame, text="一键日服务器", command=lambda: 一键日服务器()).grid(row=1, column=1,
                                                                                sticky="ew", padx=5,
                                                                                pady=5)
    ttk.Button(frame, text="一键顺着网线砍人", command=lambda: 一键顺着网线砍人()).grid(row=2, column=0,
                                                                                        sticky="ew", padx=5,
                                                                                        pady=5)
    ttk.Button(frame, text="一键给对手戴绿帽", command=lambda: 一键给对手戴绿帽()).grid(row=2, column=1,
                                                                                        sticky="ew", padx=5,
                                                                                        pady=5)
    ttk.Button(frame, text="一键召唤陨石砸向对手", command=lambda: 一键召唤陨石砸向对手()).grid(row=3,
                                                                                                column=0,
                                                                                                sticky="ew",
                                                                                                padx=5,
                                                                                                pady=5)
    ttk.Button(frame, text="一键拔掉对方网线", command=lambda: 一键拔掉对方网线()).grid(row=3, column=1,
                                                                                        sticky="ew", padx=5,
                                                                                        pady=5)
    ttk.Button(frame, text="一键盗QQ号", command=lambda: 一键盗QQ号()).grid(row=4, column=0, sticky="ew",
                                                                            padx=5, pady=5)
    ttk.Button(frame, text="一键日进内网", command=lambda: 一键日进内网()).grid(row=4, column=1, sticky="ew",
                                                                                padx=5, pady=5)
    ttk.Button(frame, text="一键挖洞", command=lambda: 一键挖洞()).grid(row=5, column=0, sticky="ew", padx=5,
                                                                        pady=5)
    ttk.Button(frame, text="一键刷Q币", command=lambda: 一键刷Q币()).grid(row=5, column=1, sticky="ew",
                                                                          padx=5, pady=5)
    ttk.Button(frame, text="一键挖比特币", command=lambda: 一键挖比特币()).grid(row=6, column=0, sticky="ew",
                                                                                padx=5, pady=5)
    ttk.Button(frame, text="一键刷会员", command=lambda: 一键刷会员()).grid(row=6, column=1, sticky="ew",
                                                                            padx=5, pady=5)
    ttk.Button(frame, text="一键日教务系统", command=lambda: 一键日教务系统()).grid(row=7, column=0,
                                                                                    sticky="ew", padx=5,
                                                                                    pady=5)
    ttk.Button(frame, text="一键社工管理员全家", command=lambda: 一键社工管理员全家()).grid(row=7, column=1,
                                                                                            sticky="ew",
                                                                                            padx=5, pady=5)
    ttk.Button(frame, text="一键DDOS", command=lambda: 一键DDOS()).grid(row=8, column=0, sticky="ew", padx=5,
                                                                        pady=5)
    ttk.Button(frame, text="一键让对方拉稀", command=lambda: 一键让对方拉稀()).grid(row=8, column=1,
                                                                                    sticky="ew", padx=5,
                                                                                    pady=5)
    ttk.Button(frame, text="一键支付宝充值100万", command=lambda: 一键支付宝充值100万()).grid(row=9, column=0,
                                                                                              columnspan=2,
                                                                                              sticky="ew",
                                                                                              padx=5, pady=5)
    # 添加退出按钮
    ttk.Button(frame, text="退出", command=root.destroy).grid(row=10, column=0, columnspan=2, sticky="ew", padx=5,
                                                              pady=10)

    # 主循环
    root.mainloop()


