import random
import threading
from queue import Queue, Empty
from util.simulateprogressbar import simulate_progress_bar
from tabulate import tabulate


def onekeyclickfucksatellite():
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
    except KeyboardInterrupt:
        queue.put(None)
