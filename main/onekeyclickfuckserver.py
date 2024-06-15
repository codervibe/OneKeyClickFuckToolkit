from utils.progressbar import simulate_progress_bar
import socket
from tqdm import tqdm





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
    # simulate_progress_bar("扫描端口", 60)
    host = input("请输入要扫描的主机地址 (例如，127.0.0.1): ")
    port_input = input("请输入要扫描的端口 (逗号分隔或 'all' 表示所有端口): ")

    print(f"正在扫描 {host} 上的指定端口...\n")
    open_ports = []

    """
        扫描指定主机的端口。

        参数:
            host (str): 目标主机地址。
            port_input (str): 要扫描的端口，逗号分隔的字符串或 'all' 表示所有端口。

        返回:
            list: 开放端口的列表。
        """
    open_ports = []

    # 处理端口输入
    if port_input.lower() == 'all':
        # 如果输入为 'all'，则设置端口范围为 1 到 65535
        ports = range(1, 65536)
    else:
        try:
            # 将输入的逗号分隔的端口字符串转换为整数列表
            ports = [int(p) for p in port_input.split(',')]
        except ValueError:
            # 输入格式错误时，提示用户
            print("无效的端口输入。请输入逗号分隔的数字或 'all'。")
            return []

    try:
        # 尝试解析主机名
        host_ip = socket.gethostbyname(host)
    except socket.gaierror:
        # 处理无法解析主机名的错误
        print(f"无法解析主机名: {host}")
        return []

    # 使用 tqdm 创建进度条
    with tqdm(total=len(ports), desc="扫描端口", unit="port") as pbar:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # 设置超时时间为1秒
            result = s.connect_ex((host, port))  # 尝试连接
            if result == 0:
                open_ports.append(port)
            s.close()
            pbar.update(1)  # 更新进度条

    if open_ports:
        print(f"开放端口: {open_ports}")
    else:
        print("未找到开放端口。")

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
