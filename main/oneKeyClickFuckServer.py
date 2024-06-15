from utils.progressbar import simulate_progress_bar

def informationcollection():
    """
    信息收集
    """
    scanningport()
    getrealiP()
    scansegmentcoftheServer()
    collectsubdomainnameinformation()
    return


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
