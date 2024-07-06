import requests
import warnings
from bs4 import BeautifulSoup
from requests.packages import urllib3
import chardet
import html
import threading
from colorama import Fore, Back, Style, init

# 初始化Colorama，使其在 Windows 终端中正常工作
init(autoreset=True)

# 关闭警告
urllib3.disable_warnings()
warnings.filterwarnings("ignore")

def get_html_content(url):
    try:
        result = requests.get(url, timeout=2, verify=False)
        result.raise_for_status()
        content = result.content
        encoding = chardet.detect(content)['encoding']
        return content, encoding
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.NORMAL + f"发生网络错误:{e}" + Style.RESET_ALL)
        return None, None

def get_title(content, encoding):
    if content:
        # 将内容从网页编码解码为Unicode字符串
        # content = content.decode(encoding)
        
        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(content, 'html.parser')
        
        # 尝试获取<title>标签中的标题
        title_tag = soup.find('title')
        if title_tag:
            title_with_entities = title_tag.get_text().strip()
            # 解码包含HTML实体编码的标题
            title = html.unescape(title_with_entities)
        else:
            title = "未找到标题"

        return title
    else:
        return None

def write_title_to_file(url, title):
    if title:
        with open("./source/html_title.txt", "a+", encoding="utf-8") as f1:
            print(Fore.GREEN + Style.NORMAL + f"{url} 的网页标题: {title}\n" + Style.RESET_ALL)
            f1.write(f"{url} 的网页标题: {title}\n")
    else:
        with open("./source/no_html_title.txt", "a+", encoding="utf-8") as f1:
            print(Fore.RED + Style.NORMAL + f"{url}  发生网络错误\n" + Style.RESET_ALL)
            f1.write(f"{url}  发生网络错误\n")


def main_get_title():
    with open("./source/urls.txt","r",encoding="utf-8") as f:
        urls = f.readlines()

    for url in urls:
        # url = "http://" + url.strip()
        url = url.strip()
        print(url)
        content, encoding = get_html_content(url)
        title = get_title(content, encoding)
        write_title_to_file(url, title)

if __name__ == "__main__":
    main_get_title()
