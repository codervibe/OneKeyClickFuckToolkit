import os
import time
from tabulate import tabulate
from pywifi import PyWiFi, const, Profile
from tqdm import tqdm
from wifi_cracker import crack_wifi, scan_wifi, connect_to_wifi, select_interface

def print_menu():
    """
    打印选择菜单.
    """
    print("\n请选择一个操作:")
    print("1. 一键日卫星")
    print("2. 一键日服务器")
    print("3. 一键破解wifi")
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
        elif choice == '0':
            print("退出程序.")
            exit()
        else:
            print("无效选择，请重新选择.")
    except KeyboardInterrupt:
        print("\n程序被用户中断.")
        exit()

def perform_scan_and_select_satellite():
    """
    执行扫描地址并选择卫星.
    """
    try:
        # 执行扫描地址
        print("扫描当前可用的地址...")
        simulate_progress_bar("扫描地址", 630)

        # 模拟扫描结果
        available_addresses = [f"192.168.1.{i}" for i in range(1, 255)]
        print("找到可用地址, 按回车键显示地址列表，或等待 3 秒自动继续。")

        # 等待用户按回车或 3 秒后继续
        user_input = wait_for_enter_or_timeout(3)

        if user_input is not None:
            # 格式化输出可用地址
            address_table = [(i + 1, address) for i, address in enumerate(available_addresses)]
            print("\n可用地址:")
            print(tabulate(address_table, headers=["序号", "地址"], tablefmt="grid"))

        # 自动选择可用卫星
        print("自动选择可用的卫星...")
        simulate_progress_bar("选择卫星", 530)

        # 模拟选择的卫星
        selected_satellite = random.choice(available_addresses)
        print(f"已选择卫星地址: {selected_satellite}")

        # 正在尝试生成字典
        print("正在尝试生成字典...")
        simulate_progress_bar("生成字典", 130, pause_at=89, pause_duration=20)

        # 正在尝试破解控制系统密码
        print("正在尝试破解控制系统密码...")
        simulate_progress_bar("破解控制系统密码", 30)

        # 尝试破解控制系统
        print("正在尝试破解控制系统...")
        simulate_progress_bar("破解控制系统", 399, pause_at=175, pause_duration=30)
        print("操作完成!\n")

    except KeyboardInterrupt:
        print("\n程序被用户中断.")
        exit()

def perform_daily_server():
    """
    执行一键日服务器.
    """
    try:
        print("正在执行一键日服务器...")
        simulate_progress_bar("一键日服务器", 89)
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

def simulate_progress_bar(action, steps, length=50, fill='█', pause_at=None, pause_duration=0):
    """
    模拟进度条的过程.
    """
    try:
        for i in range(steps + 1):
            percent = ("{0:.1f}").format(100 * (i / float(steps)))
            filled_length = int(length * i // steps)
            bar = fill * filled_length + '-' * (length - filled_length)
            print(f'\r|{bar}| {percent}% {action}', end='\r')

            # 检查是否到达暂停点
            if pause_at and i == pause_at:
                time.sleep(pause_duration)  # 暂停指定时间

            time.sleep(0.05)  # 模拟任务的延迟
        print()  # 完成后换行
    except KeyboardInterrupt:
        print("\n操作被中断.")
        exit()

def wait_for_enter_or_timeout(timeout):
    """
    等待用户按回车键或超时后继续.
    """
    input_queue = Queue()
    input_thread = threading.Thread(target=input_with_timeout, args=(input_queue,))
    input_thread.daemon = True
    input_thread.start()

    # 等待 timeout 秒或用户输入
    try:
        return input_queue.get(timeout=timeout)
    except Empty:
        return None  # 超时继续，不输出地址列表

def input_with_timeout(queue):
    """
    等待用户输入，将输入结果放入队列.
    """
    try:
        user_input = input()
        queue.put(user_input)
    except Exception:
        queue.put(None)

def main():
    try:
        while True:
            print_menu()
            choice = input("PS>")
            perform_action(choice)
    except KeyboardInterrupt:
        print("\n程序已退出.")

if __name__ == "__main__":
    main()
