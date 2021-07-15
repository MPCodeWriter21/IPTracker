# Variables

__all__ = ['UserAgent', 'proxy', 'socks5_proxy', 'http_proxy', 'horizontal_line', 'Colors', 'a', 'p', 'n', 'banner']

UserAgent = "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
proxy = False
socks5_proxy = ''
http_proxy = ''


# Returns a horizontal line
def horizontal_line():
    import os
    return '=' * (os.get_terminal_size()[0] - 1)


# Colors
class Colors:
    Default = '\033[0m'
    Gray = '\033[90m'
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Pink = '\033[95m'
    Cyan = '\033[96m'
    BCyan = '\033[1;96m'
    White = '\033[1;37m'

    BackGray = '\033[100m'
    BackRed = '\033[101m'
    BackGreen = '\033[102m'
    BackYellow = '\033[103m'
    BackPurple = '\033[104m'
    BackPink = '\033[105m'
    BackCyan = '\033[106m'
    BackWhite = '\033[107m'


a = f'{Colors.Cyan}[\033[35m={Colors.Cyan}] ' + Colors.Default
p = f'{Colors.Yellow}[{Colors.Green}+{Colors.Yellow}] ' + Colors.Default
n = f'{Colors.Yellow}[{Colors.Red}-{Colors.Yellow}] ' + Colors.Default

e = Colors.White + horizontal_line() + Colors.Default

banner = f"""{e + Colors.Red}
 ___ ____    _____               _
|_ _|  _ \  |_   _| __ __ _  ___| | _____ _ __
 | || |_) |   | || '__/ _` |/ __| |/ / _ \ '__|
 | ||  __/    | || | | (_| | (__|   <  __/ |
|___|_|  {Colors.Green}v\033[33m1.1{Colors.Red} |_||_|  \__,_|\___|_|\_\___|_|
{Colors.White}{e}
{Colors.White}Blog    {Colors.Red} :{Colors.Cyan} https://www.{Colors.BCyan}CodeWriter21{Colors.Cyan}.blogsky.com
{Colors.White}Github  {Colors.Red} :{Colors.Cyan} http://www.GitHub.com/{Colors.BCyan}MPCodeWriter21
{Colors.White}Telegram{Colors.Red} :{Colors.Cyan} https://www.Telegram.me/{Colors.BCyan}CodeWriter21
{Colors.White}{e}"""
