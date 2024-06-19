import os
import platform
import time

# ANSI颜色码
COLORS = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
}

def simulate_progress_bar(action, steps, length=50, fill='█', pause_at=None, pause_duration=0):
    """
    模拟进度条的过程.
    """
    """
        模拟带颜色的进度条的过程.

        参数:
        - action: 正在执行的动作的描述。
        - steps: 总步数，表示任务总共需要完成的步数。
        - length: 进度条的长度，默认为50个字符。
        - fill: 用来填充进度条的字符，默认为 '█'。
        - pause_at: 暂停的步数点，默认为None，表示不暂停。
        - pause_duration: 暂停时的持续时间，单位为秒，默认为0。

        返回:
        - 无
        """
    try:
        for i in range(steps + 1):
            percent = "{0:.1f}".format(100 * (i / float(steps)))
            filled_length = int(length * i // steps)
            bar = fill * filled_length + '-' * (length - filled_length)

            # 根据进度百分比改变颜色
            if float(percent) < 30:
                color = COLORS['FAIL']
            elif float(percent) < 60:
                color = COLORS['WARNING']
            else:
                color = COLORS['OKGREEN']

            # ANSI转义序列用于改变颜色
            colored_bar = f"{color}|{bar}|{COLORS['ENDC']}"

            # 打印进度条、百分比和动作描述
            print(f'\r{colored_bar} {percent}% {action}', end='\r')

            # 检查是否到达暂停点
            if pause_at and i == pause_at:
                time.sleep(pause_duration)  # 暂停指定时间

            time.sleep(0.05)  # 模拟任务的延迟

        print()  # 完成后换行
    except KeyboardInterrupt:
        print("\n操作被中断.")
        exit()
def getsTheRequiredFilesInResource(filename):
    if platform.system() == "Windows":
        # 获取当前脚本文件的绝对路径
        # 进入到resource文件夹
        resource_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                       'resource')
        # 指纹文件的路径
        return os.path.join(resource_folder, filename)

    else:
        return os.path.join(os.path.expanduser("~"), filename)