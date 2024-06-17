from onekeyclickfucksatellite import onekeyclickfucksatellite
from onekeyclickfuckserver import informationcollection


def print_menu():
    """
    打印选择菜单.
    """
    print("\n请选择一个操作:")
    print("1. 一键日卫星")
    print("2. 一键日服务器")
    print("0. 退出")


def perform_action(choice):
    """
    根据用户选择执行相应的操作.
    """
    try:
        if choice == '1':
            perform_scan_and_select_satellite()
        elif choice == '2':
            perform_daily_server()
        elif choice == '0':
            print("退出程序.")
            exit()
        else:
            print("无效选择，请重新选择.")
    except KeyboardInterrupt:
        print("\n程序被用户中断.")
        exit()


def main():
    try:
        while True:
            print_menu()
            choice = input("PS>")
            perform_action(choice)
    except KeyboardInterrupt:
        print("\n程序已退出.")


def perform_daily_server():
    """
    执行一键日服务器.
    """
    try:
        print("正在执行一键日服务器...")
        # simulate_progress_bar("一键日服务器", 89)
        informationcollection()
        print("一键日服务器完成!\n")
    except KeyboardInterrupt:
        print("\n程序被中断.")
        exit()


def perform_scan_and_select_satellite():
    try:
        onekeyclickfucksatellite()
    except KeyboardInterrupt:
        print("\n程序被中断.")
        exit()


if __name__ == "__main__":
    main()
