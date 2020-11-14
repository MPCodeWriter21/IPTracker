# IP Tracker

IP Tracker is a Python script which you can use in order to receive IP informations.

It's totally free and ready to use. You can install it using the guide below and start using it without any problem whatsoever.

## About

My Telegram: [@MehradP21](https://t.me/MehradP21)

My Telegram Channel: [@CodeWriter21](https://t.me/CodeWriter21)

My Blog: [CodeWriter21.blogsky.com](http://CodeWriter21.blogsky.com)

## Installation

In order to use this you'll need to install some packages and Python libraries.

### Installing Python

Linux:
> apt-get install python

Windows:
> Get the latest version from [https://www.python.org](https://www.python.org)

### Installing curl (No need for Windows)

> apt-get install curl

### Installing pip

Linux:
> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
> python get-pip.py

Windows:
> Download the get-pip Python file: [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py)

> python get-pip.py

### Installing required libraries with pip 
(The same on both Windows and Linux)

### Automatically
You can enter command bellow or install libraries manually

> pip install -r requirements.txt

### Manually

#### requests

> pip install requests

#### Beautiful Soup

> pip install bs4

#### whois

> pip install whois

## Usage

> python run.py [OPTIONS]

    --hostname, -name, -ip   <HOSTNAME or IP ADDRESS>        - if sets, won't see Enter Target IP
                                                               message
    --whois, -w              <True or False>                 - if sets as True, IP will be WHOISed
                                                               without prompt
                                                             - if sets as False, IP won't be
                                                               WHOISed without prompt
    --socks-proxy, -s        [<SOCKS5 Proxy> : <Proxy Port>] - sets SOCKS5 proxy to WHOIS ip
    --http-proxy, -h         [<HTTP Proxy> : <Proxy Port>]   - sets HTTP/HTTPS proxy to WHOIS ip
    --myip, -m                                               - use this switch to track your ip
    --help, -help

### Example

> python run.py -m --whois True

It will track your IP and WHOIS it without prompt

> python run.py -name google.com

It will track Google.com
