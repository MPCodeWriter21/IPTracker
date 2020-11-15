try:
	import os, sys, socket, requests, json
	from time import sleep
	from bs4 import BeautifulSoup
	import whois as Whois
	from sys import argv as args
except ModuleNotFoundError as e:
	print ("\033[91mCouldn't import library: \033[33m" + str(e))
	print ("\033[91mPlease install requirements: \033[33mpip install -r requirements.txt\033[0m")
	exit()



ua={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
proxy = False
sproxy = ''
hproxy = ''

end = '\033[0m'

R = '\033[91m'
G = '\033[92m'
P = '\033[95m'
W = '\033[1;37m'
Y = '\033[93m'
C = '\033[1;96m'
c = '\033[0;96m'
r = '\033[0;31m'

a = '\033[36;1m[\033[35;1m=\033[36;1m] ' + end
p = '\033[1;34m[\033[1;92m+\033[1;34m] ' + end
n = '\033[1;34m[\033[1;93m-\033[1;34m] ' + end

e = W + '===============================================' + end

#o = '\033[0;34m[+]\033[1;37m MAPS         \033[0;31m:\033[0;32m '

banner = f"""{e + R}
 ___ ____    _____               _
|_ _|  _ \  |_   _| __ __ _  ___| | _____ _ __
 | || |_) |   | || '__/ _` |/ __| |/ / _ \ '__|
 | ||  __/    | || | | (_| | (__|   <  __/ |
|___|_|  {G}v\033[33m1.0{R} |_||_|  \__,_|\___|_|\_\___|_|
{W}===============================================
{W}Blog    {r} :{c} https://www.{C}CodeWriter21{c}.blogsky.com
{W}Github  {r} :{c} http://www.GitHub.com/{C}MPCodeWriter21
{W}Telegram{r} :{c} https://www.Telegram.me/{C}CodeWriter21
{W}==============================================="""

help = f"""
{G}usage: {P}python {W}run.py [{Y}OPTIONS{W}]

\t{Y}--hostname{W}, {Y}-name{W}, {Y}-ip{W} \t <{P}HOSTNAME{W} or {P}IP ADDRESS{W}>        - if sets, won't see Enter Target IP
\t                       \t                                   message
\t{Y}--whois{W}, {Y}-w{W}            \t <{P}True{W} or {P}False{W}>                 - if sets as True, IP will be whoised
\t                                                           without prompt
\t                       \t                                 - if sets as False, IP won't be
\t                                                           whoised without prompt
\t{Y}--socks-proxy{W}, {Y}-s{W}      \t [<{P}SOCKS5 Proxy{W}> : <{P}Proxy Port{W}>] - sets SOCKS5 proxy to whois ip
\t{Y}--http-proxy{W}, {Y}-h{W}       \t [<{P}HTTP Proxy{W}> : <{P}Proxy Port{W}>]   - sets HTTP/HTTPS proxy to whois ip
\t{Y}--myip{W}, {Y}-m{W}             \t                                 - use this switch to track your ip
\t{Y}--help{W}, {Y}-help{W}          \t                                 - shows this help text
"""

#Prints Exit and then exits
def exit(text = ''):
	if text:
		print (text)
		print (e)
	sys.exit(a + "\033[31;1mExit" + end)

#Checks if user is connected to Internet
def check_connection():
	print (a + "\033[93mChecking Internet Connection...\r\033[0m", end = '')
	try:
		requests.get("https://ip-api.com")
		print ('                                    \r', end = '')
	except requests.exceptions.ConnectionError:
		print ('                                    \r', end = '')
		exit(n + "\033[91mConnection Error!!\n" + 
			n + "\033[31mCheck your Internet connection and your VPN/Proxy/DNS if you are using..." + end)
	except KeyboardInterrupt:
		print ('                                    \r', end = '')
		exit('\r' + n + '\033[91mCancelled!' + end)
	except:
		print ('                                    \r', end = '')
		exit(n + '\033[91mAn unknown error occurred!!' + end)
	print ('                                    \r', end = '')


#Finds the IP of Host by HostName
def get_ip(name):
	try:
		return socket.gethostbyname(name)
	except:
		return 'Wrong HostName'

#Checks if the input is a valid IP
def is_IP(ip):
	try:
		parts = ip.split('.')
		if len(parts) != 4:
			return False
		for p in parts:
			if int(p)<0 or int(p)>255:
				return False
		if int(parts[0]) == 0:
			return False
		return True
	except:
		return False

#Prints the word is unknown (if couldn't find any info about it)
def unknown(word):
	spaces = '            '
	for l in word:
		spaces += '\b'
	print (n + word + spaces + '\033[1;91m: \033[2;33m Unknown' + end)

#Prints the word and its value(actually information about it)
def known(word, data):
	if (not word) or (not data):
		return
	spaces = '            '
	for l in word:
		spaces += '\b'
	print (p + W + word + spaces + '\033[1;91m:\033[0;32m ' + str(data))

#Tries to get WHOIS information from Whois.com
def whois1(ip):
	try:
		url = "https://www.whois.com/whois/" + ip
		if proxy:
			if hproxy:
				prx = {'http': 'http://'+hproxy, 'https': 'http://'+hproxy }
			if sproxy:
				prx = {'http': 'socks5://'+sproxy, 'https': 'socks5://'+sproxy }
		req = requests.get(url, ua)
		soup = BeautifulSoup(req.text, 'html.parser')
		sleep(2)
		data = soup.find('pre', class_="df-raw", id = "registryData").text
		ds = data.split('\n')
		data = []
		for l in ds:
			if l == '':
				continue
			if l[0] == '%' or l[0] == '#' or l[0] == '>':
				continue
			l = l.replace(' ', '')
			index = l.find(':')
			data.append([l[:index], l[index+1:]])
		if not data:
			print(n + "\033[95mCouldn't find WHOIS data!!" + end)
		else:
			for d in data:
				known(d[0], d[1])
	except KeyboardInterrupt:
		exit('\r' + n + '\033[91mCancelled!' + end)
	except AttributeError:
		exit(n + f'\033[91mAn error occurred: Try opening "{url}"' + end)
	except:
		exit(n + '\033[91mAn unknown error occurred!!' + end)
	print (e)

def whois(ip):
	try:
		print (e)
		query = Whois.query(ip)
		query = query.__dict__
		if query:
			for item in query:
				if not type(query[item]) is set:
					known(item, query[item])
				else:
					for i in query[item]:
						known(item, i)
	except KeyboardInterrupt:
		exit(f'\r' + n + '\033[91mCancelled!' + end)
	except:
		return
	print (e)

#Main Function Of Script
def run():
	print (banner)
	check_connection()
	name = ''
	bwhois = None
	global proxy, sproxy, hproxy
	for i in range(len(args)):
		if args[i] == '-help' or args[i] == '--help':
			ezit(help)
		
		if args[i] == '-m' or args[i] == '--myip':
			name = requests.get("http://icanhazip.com/").content.decode()
			name = name[:len(name)-1]
		
		try:
			if args[i] == '--hostname' or args[i] == '-name' or args[i] == '-ip':
				name = args[i+1]
			if args[i] == '--whois' or args[i] == '-w':
				if args[i+1].lower() == 'true':
					bwhois = True
				elif args[i+1].lower() == 'false':
					bwhois = False
				else:
					exit(n + "\033[91m'{args[i]}' needs True or False as argument!" + end)
			if args[i] == '--socks-proxy' or args[i] == '-s':
				proxy = True
				sproxy = args[i+1]
			if args[i] == '--http-proxy' or args[i] == '-h':
				proxy = True
				hproxy = args[i+1]
		except IndexError:
			exit(a + f"\033[91m\033[91m'{args[i]}' needs an argument!" + end)
	
	try:
		#Takes input and checks it
		if not name:
			name = input(a + "\033[37;1mEnter Target IP or Hosname\033[31;1m :\033[32;1m ")
		ip = name
		try:
			if not name:
				print (n + "\033[31mInput Is Empty!!" + end)
				self_ip = input(a + "Do you want to track your IP?(\033[32mY\033[0m/\033[31;1mN\033[37;1m) \033[31;1m:\033[32;1m ").lower()
				if self_ip == 'y':
					ip = requests.get("http://icanhazip.com/").content.decode()
					ip = ip[:len(ip)-1]
					name = ip
				else:
					print (e)
					exit()
			if not is_IP(name):
				ip = get_ip(name)
				if not is_IP(ip):
					exit(n + "\033[91mEnterd Data is wrong!" + end)
			os.system('clear')
			print(banner)
			print(a + "\033[0;36mSearching for \033[1;96m"+(name if ip == name else (name+' \033[1;91m(\033[1;36m '+ip+' \033[1;91m)'))+"\033[0m")
			print(e)
			if not name:
				name = ip
		except KeyboardInterrupt:
			exit('\r' + n + '\033[91mCancelled!' + end)
		print (a + "\033[37;1mPlease Wait" + end)
		sleep(2)
		print (e)
		#Tries to get information about IP
		url = "http://ip-api.com/json/" + ip
		try:
			data = requests.get(url).content.decode()
		except requests.exceptions.ConnectionError:
			exit(n + "\033[91mConnection Error!!\n" +
				n + "\033[31mCheck your Internet connection and your VPN/Proxy/DNS if you are using..." + end)
		data2 = json.loads(data)
		del data
		#Prints Information of the IP
		try:
			known('AS', data2["as"])
		except KeyError:
			unknown('AS')
		try:
			known('COUNTRY', data2['country'])
		except KeyError:
			unknown('COUNTRY')
		try:
			known('CITY', data2['city'])
		except KeyError:
			unknown('CITY')
		try:
			known('COUNTRY CODE', data2['countryCode'])
		except KeyError:
			unknown('COUNTRY CODE')
		try:
			known('ISP', data2['isp'])
		except KeyError:
			unknown('ISP')
		try:
			known('LATITUDE', data2['lat'])
		except KeyError:
			unknown('LATITUDE')
		try:
			known('LONGTITUDE', data2['lon'])
		except KeyError:
			unknown('LONGTITUDE')
		try:
			known('ORG', data2['org'])
		except KeyError:
			unknown('ORG')
		try:
			known('QUERY', data2['query'])
		except KeyError:
			unknown('QUERY')
		try:
			known('REGION', data2['region'])
		except KeyError:
			unknown('REGION')
		try:
			known('REGION NAME', data2['regionName'])
		except KeyError:
			unknown('REGION NAME')
		try:
			known('TIME ZONE', data2['timezone'])
		except KeyError:
			unknown('TIME ZONE')
		try:
			known('ZIP', data2['zip'])
		except KeyError:
			unknown('ZIP')
		try:
			known('MAPS', 'https://www.google.co.id/maps/place/' + str(data2["lat"]) + ',' +  str(data2["lon"]))
		except KeyError:
			unknown('MAPS')
		try:
			if not str(data2['status']) == "fail":
				print (n + '\033[1;37mSTATUS      \033[1;91m:\033[1;32m ' + str(data2["status"]))
			else:
				known('STATUS', str(data2["status"]))
		except KeyError:
			unknown('STATUS')
		print(e)
		del data2

		#Asks user to WHOIS IP
		who = ''
		if bwhois is None:
			who = input(a + "\033[37;1mDo You Want To Try WHOIS \033[1;93m"+name+"\033[37;1m?(\033[32mY\033[0m/\033[31;1mN\033[37;1m) \033[31;1m:\033[32;1m ").lower()
		if who == 'y' or bwhois:
			print (a + "\033[37;1mPlease Wait" + end)
			whois(name)
			whois1(ip)
		elif bwhois is None:
			print (e)
		#Exits
		exit()
	except KeyboardInterrupt:
		exit('\r' + n + '\033[91mCancelled!' + end)
	except requests.exceptions.ConnectionError:
		exit(n + "\033[91mConnection Error!!\n" + 
			n + "\033[31mCheck your Internet connection and your VPN/Proxy/DNS if you are using..." + end)


if __name__=='__main__':
   run()

