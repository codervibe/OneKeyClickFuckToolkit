from main.python.CMSIdentifier import cmsFingerprintRecognition
from main.python.crack_wifi_handshake import crack_wifi_handshake
from main.python.onekeyclickfucksatellite import onekeyclickfucksatellite
from main.python.onekeyclickfuckserver import informationcollection
from main.python.wifi_cracker import crack_wifi


def print_menu():
    """
    打印选择菜单.
    """
    print("\n请选择一个操作:")
    print("1. 一键日卫星")
    print("2. 一键日服务器")
    print("3. 一键破解wifi")
    print("4. 破解wifi握手包")
    print("5. 一键CMS指纹识别")
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
        elif choice == '3':
            crack_wifi_main()
        elif choice == '4':
            crack_wifihandshake()
        elif choice == '5':
            oneClickFingerprintRecognition()
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


def oneClickFingerprintRecognition():
    try:
        cmsFingerprintRecognition()
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


def crack_wifi_main():
    """
    执行一键破解wifi.
    """
    try:
        crack_wifi()
    except KeyboardInterrupt:
        print("\n程序被中断.")
        exit()


def perform_scan_and_select_satellite():
    try:
        onekeyclickfucksatellite()
    except KeyboardInterrupt:
        print("\n程序被中断.")
        exit()


def crack_wifihandshake():
    try:
        crack_wifi_handshake()
    except KeyboardInterrupt:
        print("\n程序被中断.")
        exit()


if __name__ == "__main__":
    main()
