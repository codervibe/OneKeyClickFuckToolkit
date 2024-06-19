import os
import platform
import random
import sys
import time

# ANSI颜色码
COLORS = {
    'OKBLUE': '\033[94m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    'BACKGROUND_BLUE': '\033[44m',
    'BACKGROUND_YELLOW': '\033[43m',
    'BLINK': '\033[5m'
}

def blink_color(color, duration):
    """
    让字符在一段时间内闪烁变色.

    参数:
    - color: ANSI颜色码.
    - duration: 闪烁的持续时间（秒）.

    返回:
    - 无
    """
    for _ in range(int(duration / 0.2)):  # 闪烁5次
        sys.stdout.write(f'\r{color}')
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f'\r{COLORS["ENDC"]}')
        sys.stdout.flush()
        time.sleep(0.1)

def random_color():
    """
    随机生成一个ANSI颜色码.

    返回:
    - ANSI颜色码
    """
    color_code = random.choice(list(COLORS.values()))
    return color_code

def simulate_progress_bar(action, steps, length=50, fill='█', pause_at=None, pause_duration=0):
    """
    模拟带多种特效的进度条的过程.

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
            percent = 100 * (i / float(steps))
            filled_length = int(length * i // steps)
            bar = fill * filled_length + '-' * (length - filled_length)

            # 随机颜色
            color = random_color()

            # ANSI转义序列用于改变颜色
            colored_bar = f"{color}|{bar}|{COLORS['ENDC']}"

            # 字符闪烁效果
            if i == steps:
                blink_color(COLORS['OKGREEN'], 2)  # 闪烁2秒

            # 背景特效
            if i % 10 == 0:
                background_color = COLORS['BACKGROUND_BLUE'] if i % 20 == 0 else COLORS['BACKGROUND_YELLOW']
                sys.stdout.write(f'\r{background_color}{colored_bar} {percent:.1f}% {action}{COLORS["ENDC"]}')
            else:
                sys.stdout.write(f'\r{colored_bar} {percent:.1f}% {action}')

            sys.stdout.flush()

            # 检查是否到达暂停点
            if pause_at and i == pause_at:
                time.sleep(pause_duration)  # 暂停指定时间

            time.sleep(0.1)  # 模拟任务的延迟

        print()  # 完成后换行
    except KeyboardInterrupt:
        print("\n操作被中断.")





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