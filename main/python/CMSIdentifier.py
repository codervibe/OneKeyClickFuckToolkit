import json
import os
import platform
import requests
from util.utils import getsTheRequiredFilesInResource

def get_http_headers(url):
    """
    获取目标URL的HTTP头信息
    """
    try:
        response = requests.head(url)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers for {url}: {e}")
        return None


def get_html_content(url):
    """
    获取目标URL的HTML内容
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching content for {url}: {e}")
        return None


def load_fingerprints(file_path):
    """
    加载CMS指纹文件
    """
    try:
        with open(file_path, 'r') as file:
            fingerprints = json.load(file)
        return fingerprints
    except Exception as e:
        print(f"Error loading fingerprints file: {e}")
        return None


def identify_cms(headers, html_content, fingerprints):
    """
    根据HTTP头信息和HTML内容识别CMS
    """
    identified_cms = []

    for cms, fingerprint in fingerprints.items():
        for header in fingerprint['headers']:
            if any(header in value for key, value in headers.items()):
                identified_cms.append(cms)
                break
        for meta in fingerprint['meta']:
            if meta in html_content:
                identified_cms.append(cms)
                break

    return identified_cms


def cmsFingerprintRecognition():
    """
    主函数，执行CMS识别流程
    """
    url = input("Enter the target URL: ")

    # 构建指纹文件的路径

    fingerprints_file = getsTheRequiredFilesInResource('cms_fingerprints.json')

    headers = get_http_headers(url)
    if headers is None:
        return

    html_content = get_html_content(url)
    if html_content is None:
        return

    fingerprints = load_fingerprints(fingerprints_file)
    if fingerprints is None:
        return

    identified_cms = identify_cms(headers, html_content, fingerprints)

    if identified_cms:
        print(f"已识别CMS{url}: {', '.join(identified_cms)}")
    else:
        print(f"没有发现CMS: {url}")


def get_fingerprints_file():
    if platform.system() == "Windows":
        # 获取当前脚本文件的绝对路径
        # 进入到resource文件夹
        resource_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                       'resource')
        # 指纹文件的路径
        return os.path.join(resource_folder, 'cms_fingerprints.json')

    else:
        return os.path.join(os.path.expanduser("~"), 'cms_fingerprints.json')
