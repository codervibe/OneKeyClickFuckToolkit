import time
import random
import sys
def print_banner():
    banner = r"""
 _       __     __                              __    
| |     / /__  / /________  ____ ___  ___  ____/ /____
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \/ __  / ___/
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/ /_/ (__  ) 
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/\__,_/____/  
        """
    print(banner)

def simulate_progress_bar(task_name, duration):
    """
    模拟一个进度条的函数。
    """
    toolbar_width = 40

    # 设置进度条
    sys.stdout.write(f"{task_name}: [{' ' * toolbar_width}]")
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # 返回到开始位置

    for i in range(toolbar_width):
        time.sleep(duration / toolbar_width / 10)
        # 通过彩色输出增加花里胡哨的效果
        color = random.choice(['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m'])
        char = random.choice(['█'])
        sys.stdout.write(f"{color}{char}\033[0m")
        sys.stdout.flush()

    sys.stdout.write("]\n")

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


def print_menu():
    """
    打印选择菜单.
    """
    print("\n请选择一个操作:")
    print("\033[96m1. 一键日卫星\033[0m")
    print("\033[96m2. 一键日服务器\033[0m")
    print("\033[96m3. 一键顺着网线砍人\033[0m")
    print("\033[96m4. 一键给对手戴绿帽\033[0m")
    print("\033[96m5. 一键召唤陨石砸向对手\033[0m")
    print("\033[96m6. 一键拔掉对方网线\033[0m")
    print("\033[96m7. 一键盗QQ号\033[0m")
    print("\033[96m8. 一键日进内网\033[0m")
    print("\033[96m9. 一键挖洞\033[0m")
    print("\033[96m10. 一键刷Q币\033[0m")
    print("\033[96m11. 一键挖比特币\033[0m")
    print("\033[96m12. 一键刷会员\033[0m")
    print("\033[96m13. 一键日教务系统\033[0m")
    print("\033[96m14. 一键社工管理员全家\033[0m")
    print("\033[96m15. 一键DDOS\033[0m")
    print("\033[96m16. 一键让对方拉稀\033[0m")
    print("\033[96m17. 一键支付宝充值100万\033[0m")
    print("\033[96m0. 退出\033[0m")


def perform_action(choice):
    """
    根据用户选择执行相应的操作.
    """
    try:
        if choice == '1':
            perform_scan_and_select_satellite()
        elif choice == '2':
            perform_daily_server()
        elif choice == '3':
            一键顺着网线砍人()
        elif choice == '4':
            一键给对手戴绿帽()
        elif choice == '5':
            一键召唤陨石砸向对手()
        elif choice == '6':
            一键拔掉对方网线()
        elif choice == '7':
            一键盗QQ号()
        elif choice == '8':
            一键日进内网()
        elif choice == '9':
            一键挖洞()
        elif choice == '10':
            一键刷Q币()
        elif choice == '11':
            一键挖比特币()
        elif choice == '12':
            一键刷会员()
        elif choice == '13':
            一键日教务系统()
        elif choice == '14':
            一键社工管理员全家()
        elif choice == '15':
            一键DDOS()
        elif choice == '16':
            一键让对方拉稀()
        elif choice == '17':
            一键支付宝充值100万()
        elif choice == '0':
            print("退出程序.")
            exit()
        else:
            print("\033[91m无效选择，请重新选择.\033[0m")
    except KeyboardInterrupt:
        print("\n\033[91m程序被用户中断.\033[0m")
        exit()


def main():
    print_banner()
    try:
        while True:
            print_menu()
            choice = input("PS> ")
            perform_action(choice)
    except KeyboardInterrupt:
        print("\n\033[91m程序已退出.\033[0m")


def perform_daily_server():
    """
    执行一键日服务器.
    """
    try:
        print("正在执行一键日服务器...")
        informationcollection()
        print("\033[92m一键日服务器完成!\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


def perform_scan_and_select_satellite():
    try:
        onekeyclickfucksatellite()
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()


if __name__ == "__main__":
    main()
