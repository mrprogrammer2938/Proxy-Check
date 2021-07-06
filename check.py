#!/usr/bin/python3
# This Programm write by Mr.nope
# Proxy-Check 1.2.1

import os, requests, sys, platform, time, socket


system = platform.uname()[0]

def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print("\nPlease, Run This Programm on Windows, Linux, MacOS\n")
        sys.exit()
def main():
    os.system("printf '\033]2;Proxy Check\a'")
    cls()
    print("-----[ Proxy Check ]-----[ Version: 1.2.1 ]\n")
    print("Usage: Ctrl + D To Exit\n")
    host = input("\nEnter host: ")
    time.sleep(1)
    proxy_fi = input("\nEnter Proxy File Name: ")
    time.sleep(1)
    proxy_op = open(proxy_fi)
    print("\n")
    host_ip = socket.gethostbyname(host)
    print("\n")
    print(f'Ip: {host_ip}\n')
    for proxy in proxy_op:
        proxy = proxy.split('\n',1)[0]
        try:
            requests.get(f"https://{host}",proxies={'http':'http://'+proxy},timeout=(3.05,27))
            l = 1
        except requests.ConnectionError:
            l = 2
            print("Proxy Offline : ",proxy)
        except requests.HTTPError:
            l = 2
            print('Proxy Offline : ',proxy)
        except requests.Timeout:
            l = 2
            print('Proxy Offline : ',proxy)
        except requests.exceptions.InvalidURL:
            l = 2
            print('Proxy Offline : ',proxy)
        except KeyboardInterrupt:
            print("\nCtrl + C")
            print("\nExiting...")
            quit
        if l == 1:
            print("Proxy Online : ",proxy)
            with open('proxy_open.txt','a') as file:
                file.write(proxy+'\n')
                file.close()
            print("\nFile: Proxy_open.txt Saved!\n")
            try1()
def try1():
    try_to_attack = input("\nDo you want to try again? [y/n] ")
    if try_to_attack == 'y':
        main()
    elif try_to_attack == 'n':
        ext()
    else:
        try1()
def try2():
    try_to_main_menu = input("\npress Enter...")
    if try_to_main_menu == '':
        main()
    else:
        main()
def ext():
    cls()
    print("\033[92mExiting...\033[0m")
    sys.exit()
if __name__ == '__main__':
    try:
        try:
            main()
        except KeyboardInterrupt:
            print("\nCtrl + C")
            print("\nProxy-Check Stop !!!\n")
            try2()
    except EOFError:
        print("\nCtrl + D")
        print("\nExiting...")
        sys.exit()