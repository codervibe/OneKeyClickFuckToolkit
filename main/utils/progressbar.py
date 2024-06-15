import time


def simulate_progress_bar(action, steps, length=50, fill='█', pause_at=None, pause_duration=0):
    """
    模拟进度条的过程.
    """
    try:
        for i in range(steps + 1):
            percent = "{0:.1f}".format(100 * (i / float(steps)))
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
