from get_domain import *
from get_title import *
from icp_check import *
import time
from colorama import Fore, Back, Style, init

# 初始化Colorama，使其在 Windows 终端中正常工作
init(autoreset=True)


# 关闭警告
urllib3.disable_warnings()
warnings.filterwarnings("ignore")


def logo():
    print(Fore.YELLOW + Style.BRIGHT + """
         _                                   ____ _       _     
    / \   _ __   __ _ _   _  __ _ _ __  / ___| |_   _| |__  
   / _ \ | '_ \ / _` | | | |/ _` | '_ \| |   | | | | | '_ \ 
  / ___ \| | | | (_| | |_| | (_| | | | | |___| | |_| | |_) |
 /_/   \_\_| |_|\__, |\__,_|\__,_|_| |_|\____|_|\__,_|_.__/ 
                   |_|                                      
        
                     违规站点资产测绘   
              安全小天地 www.anquanclub.cn
             
          """ + Style.RESET_ALL)

if __name__ == "__main__":
    logo()
    time.sleep(1)
    print(Fore.GREEN + Style.BRIGHT + "\n开始查询存活WEB并获取WebTitle~~~\n" + Style.RESET_ALL)
    try:
        main_get_title()
    except:
        print(Fore.GREEN + Style.BRIGHT + "\n请将需要检测的url文件保存在./source/urls.txt文件中\n" + Style.RESET_ALL)
        exit()
    time.sleep(2)
    print(Fore.GREEN + Style.BRIGHT + "\n开始获取存活WEB资产根域名~~~\n" + Style.RESET_ALL)
    main_get_domain()
    time.sleep(2)
    print(Fore.GREEN + Style.BRIGHT + "\n开始获取存在备案信息的网站~~~\n" + Style.RESET_ALL)
    proxy_check()
    time.sleep(2)
    print(Fore.GREEN + Style.BRIGHT + "\n程序运行结束，请查看source目录下的备案信息、html_title文件获取违规站点,欢迎下次使用~~~\n" + Style.RESET_ALL)
