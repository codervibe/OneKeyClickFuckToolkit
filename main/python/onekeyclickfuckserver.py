from util.simulateprogressbar import simulate_progress_bar
import socket

from tqdm import tqdm


def informationcollection():
    """
    信息收集
    """
    try:
        scanningport()
        getrealiP()
        scansegmentcoftheServer()
        collectsubdomainnameinformation()
    except KeyboardInterrupt:
        print("\n\033[91m程序被中断.\033[0m")
        exit()

    # return


def scanningport():
    """
    扫描端口
    """
    simulate_progress_bar("扫描端口", 60)
    return


def getrealiP():
    """
    获取真实IP
    """
    simulate_progress_bar("获取真实IP", 60)
    return


def scansegmentcoftheServer():
    """
    扫描服务器C段
    """
    simulate_progress_bar("扫描服务器C段", 60)
    return


def collectsubdomainnameinformation():
    """
    子域名信息收集
    """
    simulate_progress_bar("子域名信息收集", 60)
    return
