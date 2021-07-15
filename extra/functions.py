# Functions

import sys
import requests
import os
import socket
import platform
from bs4 import BeautifulSoup
import whois as Whois
from colorama import AnsiToWin32 as AnsiToWin
from .variables import Colors, a, p, n, http_proxy, socks5_proxy, proxy, UserAgent, horizontal_line

__all__ = ['print', 'input', 'exit', 'horizontal_line', 'check_connection', 'get_ip', 'is_ip', 'unknown', 'known',
           'whois']

ATW = AnsiToWin(sys.stdout)
if 'windows' in platform.system().lower():
    write_text = ATW.write_and_convert
else:
    write_text = ATW.write

session = requests.session()

inputbackup = input


# Colorful print
def print(*args, end='\n'):
    text = ' '.join([str(arg) for arg in args] + [str(end)])
    if text.startswith('\r'):
        write_text('\r' + ' ' * (os.get_terminal_size()[0] - 1) + '\r')
    write_text(text)


# Colorful input
def input(*args, end=''):
    print(*args, end=end)
    return inputbackup('')


# Prints Exit and then exits
def exit(text=''):
    if text:
        print(text)
        print(Colors.White + horizontal_line() + Colors.Default, end='')
    print(a + Colors.Red + "Exit" + Colors.Default)
    sys.exit()


# Checks if user is connected to Internet
def check_connection():
    print(a + Colors.Yellow + "Checking Internet Connection..." + Colors.Default, end='')
    try:
        session.get("https://ip-api.com")
        print('\r', end='')
    except requests.exceptions.ConnectionError:
        exit('\r' + n + Colors.Red + "Connection Error!!\n" +
             n + Colors.Red + "Check your Internet connection and your VPN/Proxy/DNS if you are using..." + Colors.Default)
    except KeyboardInterrupt:
        exit('\r' + n + Colors.Red + 'Cancelled!' + Colors.Default)
    except EOFError:
        exit('\r')
    except:
        exit('\r' + n + Colors.Red + 'An unknown error occurred!!' + Colors.Default)


# Finds the IP of Host by HostName
def get_ip(name):
    try:
        return socket.gethostbyname(name)
    except:
        return 'Wrong HostName'


# Checks if the input is a valid IP
def is_ip(ip):
    try:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False
        if int(parts[0]) == 0:
            return False
        return True
    except:
        return False


# Prints the word is unknown (if couldn't find any info about it)
def unknown(word):
    spaces = '            '
    for _ in word:
        spaces += '\b'
    print(n + word + spaces + Colors.Red + ':' + Colors.Yellow + 'Unknown' + Colors.Default)


# Prints the word and its value(actually information about it)
def known(word, data):
    if (not word) or (not data):
        return
    spaces = '            '
    for _ in word:
        spaces += '\b'
    print(p + Colors.White + word + spaces + Colors.Red + ':' + Colors.Green + str(data).strip())


# Tries to get WHOIS information from Whois.com
def whois(name):
    try:
        session.headers['User-Agent'] = UserAgent
        url = "https://www.whois.com/whois/" + name
        if proxy:
            prx = {}
            if http_proxy:
                prx = {'http': 'http://' + http_proxy, 'https': 'http://' + http_proxy}
            if socks5_proxy:
                prx = {'http': 'socks5://' + socks5_proxy, 'https': 'socks5://' + socks5_proxy}
            session.proxies = prx
        req = session.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        data = soup.find('pre', class_="df-raw", id="registryData").text
        data_lines = data.split('\n')
        data = []
        for line in data_lines:
            if line == '':
                continue
            if line.startswith('%') or line.startswith('#') or line.startswith('>'):
                continue
            line = line.replace(' ', '')
            index = line.find(':')
            data.append([line[:index], line[index + 1:]])
        if not data:
            print(n + Colors.Pink + "Couldn't find WHOIS data!!" + Colors.Default)
        else:
            for row in data:
                known(row[0], row[1])
    except KeyboardInterrupt:
        exit('\r' + n + Colors.Red + 'Cancelled!' + Colors.Default)
    except EOFError:
        exit()
    except AttributeError:
        print(n + Colors.Red + f'An error occurred: Try opening "{url}"' + Colors.Default)
        return
    except:
        print(n + Colors.Red + 'An unknown error occurred!!' + Colors.Default)
        return
