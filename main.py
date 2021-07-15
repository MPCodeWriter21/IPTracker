try:
    from extra.imports import *
except ModuleNotFoundError as ex:
    print("\033[91mCouldn't import library: \033[33m" + str(ex))
    print("\033[91mPlease install requirements: \033[33mpip install -r requirements.txt\033[0m")
    exit()

session = requests.session()


# Main Function Of Script
def main():
    print(banner, end='')
    check_connection()

    name = ''
    bwhois = None
    global proxy, socks5_proxy, http_proxy

    parser = argparse.ArgumentParser()
    # options = parser.add_argument_group('Options')
    parser.add_argument('--hostname', '-name', '-n', metavar='<Host Name>', action='store', type=str, dest='hostname',
                        help='Hostname to track')
    parser.add_argument('--address', '-ip', metavar='<IP Address>', action='store', type=str, dest='ip',
                        help='IP address to track')
    parser.add_argument('--my-ip', '-m', action='store_true', dest='myip',
                        help='Use this switch to track your ip')
    parser.add_argument('--whois', '-w', action='store_true', dest='whois',
                        help='Use this switch to whois host without prompting')
    parser.add_argument('--no-whois', '-W', action='store_true', dest='no_whois',
                        help='Use this switch to whois host without prompting')
    parser.add_argument('--socks5-proxy', '-s', metavar='<SOCKS5 Proxy>', action='store', type=str, dest='socks5',
                        help='SOCKS5 Proxy(Example: 127.0.0.1:9050)')
    parser.add_argument('--http-proxy', '-H', metavar='<HTTP/HTTPS Proxy>', action='store', type=str, dest='http',
                        help='HTTP/HTTPS Proxy(Example: 127.0.0.1:8000)')
    args = parser.parse_args()

    if (args.hostname and args.ip) or (args.hostname and args.myip) or (args.myip and args.ip):
        exit(n + Colors.Red + 'Use only one of "hostname" or "address" or "my-ip" options!' + Colors.Default)
    if args.whois and args.no_whois:
        exit(n + Colors.Red + 'You can\'t use "whois" and "no-whois" together!' + Colors.Default)

    if args.hostname:
        name = args.hostname
    elif args.ip:
        name = args.ip
    elif args.myip:
        name = session.get("http://icanhazip.com/").content.decode()
        name = name[:len(name) - 1]

    if args.whois:
        bwhois = True
    if args.no_whois:
        bwhois = False

    global proxy, socks5_proxy, http_proxy
    socks5_proxy = args.socks5
    http_proxy = args.http
    if socks5_proxy or http_proxy:
        proxy = True

    try:
        # Takes input and checks it
        if not name:
            name = input(a + Colors.White + 'Enter Target IP or Hosname' + Colors.Red + ' : ' + Colors.Green)
        ip = name
        try:
            if not name:
                print(n + Colors.Red + 'Input Is Empty!!' + Colors.Default)
                self_ip = input(
                    a + 'Do you want to track your IP?' +
                    f'{Colors.White}({Colors.Green}Y{Colors.Default}/{Colors.Red}N{Colors.White}) {Colors.Red}: ' +
                    Colors.Green).lower()
                if self_ip == 'y':
                    ip = session.get('http://icanhazip.com/').content.decode()
                    ip = ip[:-1]
                    name = ip
                else:
                    print(Colors.White + horizontal_line() + Colors.Default, end='')
                    exit()
            if not is_ip(name):
                ip = get_ip(name)
                if not is_ip(ip):
                    exit(n + Colors.Red + 'Entered Data is wrong!' + Colors.Default)
            os.system('clear || cls')
            print(banner)
            print(a + Colors.Cyan + "Searching for " + Colors.BCyan + (
                name if ip == name else (
                        name + Colors.Red + ' ( ' + Colors.BCyan + ip + Colors.Red + ' )')) + Colors.Default)
            print(Colors.White + horizontal_line() + Colors.Default, end='')
            if not name:
                name = ip
        except KeyboardInterrupt:
            exit('\r' + n + Colors.Red + 'Cancelled!' + Colors.Default)
        print(a + Colors.White + "Please Wait" + Colors.Default)
        print(Colors.White + horizontal_line() + Colors.Default, end='')
        # Tries to get information about IP
        url = "http://ip-api.com/json/" + ip
        data = '{}'
        try:
            data = session.get(url).content.decode()
        except requests.exceptions.ConnectionError:
            exit(n + Colors.Red + "Connection Error!!\n" +
                 n + Colors.Red + "Check your Internet connection and your VPN/Proxy/DNS if you are using..." + Colors.Default)
        data = json.loads(data)
        # Prints Information of the IP
        try:
            known('AS', data["as"])
        except KeyError:
            unknown('AS')
        try:
            known('COUNTRY', data['country'])
        except KeyError:
            unknown('COUNTRY')
        try:
            known('CITY', data['city'])
        except KeyError:
            unknown('CITY')
        try:
            known('COUNTRY CODE', data['countryCode'])
        except KeyError:
            unknown('COUNTRY CODE')
        try:
            known('ISP', data['isp'])
        except KeyError:
            unknown('ISP')
        try:
            known('LATITUDE', data['lat'])
        except KeyError:
            unknown('LATITUDE')
        try:
            known('LONGTITUDE', data['lon'])
        except KeyError:
            unknown('LONGTITUDE')
        try:
            known('ORG', data['org'])
        except KeyError:
            unknown('ORG')
        try:
            known('QUERY', data['query'])
        except KeyError:
            unknown('QUERY')
        try:
            known('REGION', data['region'])
        except KeyError:
            unknown('REGION')
        try:
            known('REGION NAME', data['regionName'])
        except KeyError:
            unknown('REGION NAME')
        try:
            known('TIME ZONE', data['timezone'])
        except KeyError:
            unknown('TIME ZONE')
        try:
            known('ZIP', data['zip'])
        except KeyError:
            unknown('ZIP')
        try:
            known('MAPS', 'https://www.google.co.id/maps/place/' + str(data["lat"]) + ',' + str(data["lon"]))
        except KeyError:
            unknown('MAPS')
        try:
            if not str(data['status']) == "fail":
                print(n + '\033[1;37mSTATUS      \033[1;91m:\033[1;32m ' + str(data["status"]))
            else:
                known('STATUS', str(data["status"]))
        except KeyError:
            unknown('STATUS')
        print(Colors.White + horizontal_line() + Colors.Default, end='')
        del data

        # Asks user to WHOIS IP
        who = ''
        if bwhois is None:
            who = input(a + Colors.White + 'Do You Want To Try WHOIS ' + Colors.Yellow + name +
                        Colors.White + '?(' + Colors.Green + 'Y' + Colors.Default + '/' + Colors.Red + 'N' + Colors.White + ') '
                        + Colors.Red + ': ' + Colors.Green).lower()
        if who == 'y' or bwhois:
            print(a + Colors.White + "Please Wait" + Colors.Default)
            try:
                whois1(name)
            except Exception as ex:
                print(n + Colors.Red + str(type(ex)) + ': ' + Colors.Yellow + str(ex) + Colors.Default)
            try:
                whois(ip)
            except Exception as ex:
                print(n + Colors.Red + str(type(ex)) + ': ' + Colors.Yellow + str(ex) + Colors.Default)
        elif bwhois is None:
            print(Colors.White + horizontal_line() + Colors.Default, end='')
        # Exits
        exit()
    except KeyboardInterrupt:
        exit('\r' + n + Colors.Red + 'Cancelled!' + Colors.Default)
    except EOFError:
        exit()
    except requests.exceptions.ConnectionError:
        exit(n + Colors.Red + "Connection Error!!\n" +
             n + Colors.Red + "Check your Internet connection and your VPN/Proxy/DNS if you are using..." + Colors.Default)


if __name__ == '__main__':
    main()
