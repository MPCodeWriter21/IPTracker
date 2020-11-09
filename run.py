try:
	import os, sys, socket, requests, json
	from time import sleep
	from bs4 import BeautifulSoup
	import whois as Whois
except ModuleNotFoundError as e:
	print ("\033[91mCouldn't import library: \033[33m" + str(e))
	print ("\033[91mPlease install requirements: \033[33mpip install -r requirements.txt")
	exit()



e = '\033[1;37m==============================================='
ua={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}

o = '\033[0;34m[+]\033[1;37m MAPS         \033[0;31m:\033[0;32m '

banner = e + """\033[91m
 ___ ____    _____               _
|_ _|  _ \  |_   _| __ __ _  ___| | _____ _ __
 | || |_) |   | || '__/ _` |/ __| |/ / _ \ '__|
 | ||  __/    | || | | (_| | (__|   <  __/ |
|___|_|  \033[92mv\033[33m1.0\033[91m |_||_|  \__,_|\___|_|\_\___|_|
\033[1;37m===============================================
\033[1;37mBlog    \033[0;31m :\033[0;96m https://www.\033[1;96mCodeWriter21\033[0;96m.blogsky.com
\033[1;37mGithub  \033[0;31m :\033[0;96m http://www.GitHub.com/\033[1;96mMPCodeWriter21
\033[1;37mTelegram\033[0;31m :\033[0;96m https://www.Telegram.me/\033[1;96mCodeWriter21
\033[1;37m==============================================="""

#Checks if user is connected to Internet
def check_connection():
	sys.stdout.write("\033[1;34m[\033[1;92m+\033[1;34m]\033[93m  Checking Internet Connection...\r\033[0m")
	sys.stdout.flush()
	try:
		requests.get("https://ip-api.com")
		sys.stdout.write('                                    \r')
		sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		sys.stdout.write('                                    \r')
		sys.stdout.flush()
		sys.exit("\033[36;1m[\033[1;91m-\033[36;1m]\033[31m  \033[91mConnection Error!!\n\033[36;1m[\033[1;91m-\033[36;1m]  \033[31mCheck your Internet connection and your VPN/Proxy/DNS if you are using...\033[0m")
	sys.stdout.write('                                    \r')
	sys.stdout.flush()


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
	print ('\033[1;34m[\033[1;93m-\033[1;34m]\033[1;37m ',word, spaces, '\033[1;91m:','\033[2;33m Unknown\033[0m')

#Prints the word and its value(actually information about it)
def known(word, data):
	if (not word) or (not data):
		return
	spaces = '            '
	for l in word:
		spaces += '\b'
	print ('\033[1;34m[\033[1;92m+\033[1;34m]\033[1;37m ',word, spaces, '\033[1;91m:\033[0;32m ' , str(data))

#Tries to get WHOIS information from Whois.com
def whois1(ip):
	try:
		url = "https://www.whois.com/whois/" + ip
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
			print("\033[36;1m[\033[1;91m-\033[36;1m]  \033[95mCouldn't find WHOIS data!!\033[0m")
		else:
			for d in data:
				known(d[0], d[1])
	except KeyboardInterrupt:
		print('\r\033[36;1m[\033[1;91m-\033[36;1m]\033[91m  Cancelled!\033[0m')
	except AttributeError:
		print('\033[36;1m[\033[1;91m-\033[36;1m]\033[91m  An error occurred: Try opening "{}"\033[0m'.format(url))
	except:
		print('\033[36;1m[\033[1;91m-\033[36;1m]\033[91m  An unknown error occurred!!\033[0m')
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
		print('\r\033[36;1m[\033[1;91m-\033[36;1m]\033[91m  Cancelled!\033[0m')
	except:
		return
	print (e)

#Prints Exit and then exits
def exit():
	sys.exit("\033[36;1m[\033[35;1m=\033[36;1m]\033[31;1m  Exit\033[0m")

#Main Function Of Script
def run():
	try:
		#Takes input and checks it
		print (banner)
		check_connection()
		name = input("\033[36;1m[\033[35;1m=\033[36;1m]\033[37;1m  Enter Target IP or Hosname\033[31;1m :\033[32;1m ")
		ip = name
		try:
			if not name:
				print("\033[36;1m[\033[1;91m-\033[36;1m]\033[31m  Input Is Empty!!\033[0m")
				self_ip = input("\033[36;1m[\033[35;1m=\033[36;1m]\033[37;1m  Do you want to track your IP?(\033[32mY\033[0m/\033[31;1mN\033[37;1m) \033[31;1m:\033[32;1m ").lower()
				if self_ip == 'y':
					ip = requests.get("http://icanhazip.com/").content.decode()
					ip = ip[:len(ip)-1]
					name = ip
				else:
					print(e)
					exit()
			if not is_IP(name):
				ip = get_ip(name)
				if not is_IP(ip):
					sys.exit("\033[36;1m[\033[1;91m-\033[36;1m]\033[31m  Enterd Data is wrong!\033[0m")
			os.system('clear')
			print(banner)
			print("\033[0;36mSearching for \033[1;96m"+(name if ip == name else (name+' \033[1;91m(\033[1;36m '+ip+' \033[1;91m)'))+"\033[0m")
			print(e)
			if not name:
				name = ip
		except KeyboardInterrupt:
			sys.exit('\r\033[36;1m[\033[1;91m-\033[36;1m]\033[91m  Cancelled!\033[0m')
		print ("\033[36;1m[\033[35;1m=\033[36;1m]\033[37;1m  Please Wait\033[0m")
		sleep(2)
		print (e)
		#Tries to get information about IP
		url = "http://ip-api.com/json/" + ip
		try:
			data = requests.get(url).content.decode()
		except requests.exceptions.ConnectionError:
			sys.exit("\033[36;1m[\033[1;91m-\033[36;1m]\033[31m  \033[91mConnection Error!!\n\033[36;1m[\033[1;91m-\033[36;1m]  \033[31mCheck your Internet connection and your VPN/Proxy/DNS if you are using...\033[0m")
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
			print ('\033[1;34m[\033[1;92m+\033[1;34m]\033[1;37m  MAPS          \033[1;91m:\033[0;32m  https://www.google.co.id/maps/place/' + str(data2["lat"]) + ',' +  str(data2["lon"]))
		except KeyError:
			print ('\033[1;34m[\033[1;93m-\033[1;34m]\033[1;37m  MAPS          \033[1;91m:\033[2;33m  Unknown\033[0m')
		try:
			if not str(data2['status']) == "fail":
				print ('\033[1;34m[\033[1;92m+\033[1;34m]\033[1;37m  STATUS        \033[1;91m:\033[1;32m ', str(data2["status"]))
			else:
				print ('\033[1;34m[\033[1;92m+\033[1;34m]\033[1;37m  STATUS        \033[1;91m:\033[1;91m ', str(data2["status"]))
		except KeyError:
			print ('\033[1;34m[\033[1;93m-\033[1;34m]\033[1;37m  STATUS        \033[1;91m:\033[1;91m Unknown\033[0m')
		print(e)
		del data2

		#Asks user to WHOIS IP
		who = input("\033[36;1m[\033[35;1m=\033[36;1m]\033[37;1m  Do You Want To Try WHOIS \033[1;93m"+name+"\033[37;1m?(\033[32mY\033[0m/\033[31;1mN\033[37;1m) \033[31;1m:\033[32;1m ").lower()
		if who == 'y':
			print ("\033[36;1m[\033[35;1m=\033[36;1m]\033[37;1m  Please Wait\033[0m")
			whois(name)
			whois1(ip)
		else:
			print (e)
		#Exits
		exit()
	except KeyboardInterrupt:
		sys.exit('\r\033[36;1m[\033[1;91m-\033[36;1m]\033[91m  Cancelled!\033[0m')
	except requests.exceptions.ConnectionError:
		sys.exit("\033[36;1m[\033[1;91m-\033[36;1m]\033[31m  \033[91mConnection Error!!\n\033[36;1m[\033[1;91m-\033[36;1m]  \033[31mCheck your Internet connection and your VPN/Proxy/DNS if you are using...\033[0m")


if __name__=='__main__':
   run()

