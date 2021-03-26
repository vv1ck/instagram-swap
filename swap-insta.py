import os
try:
	import requests
	import threading
	import tkinter
except:
	os.system("pip install tkinter")
	os.system("pip install requests")
	os.system("pip install threading")
os.system('clear')
ms = 'H&PUQKX&Fz4{u'
c = 6
import requests , threading
from tkinter import Tk
from tkinter import messagebox
r = requests.session()
txt = list(ms)
cod = c
lst = []
for ok in txt:
	od = ord(ok)
	new = chr(od-cod)
	lst.append(new)
ok=''.join(lst)
def swap():
	global eml,num,bio,name,ext,user2,go
	while True:
		sis = go.cookies['sessionid']
		urED = 'https://www.instagram.com/accounts/edit/'
		hedED = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'content-length': '123',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; ds_user_id=45872034997; shbid=6144; csrftoken=uGeaBdGt8EF51aBV8x1MHP2aizo1Boye; rur=RVA; sessionid='+sis,
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/accounts/edit/',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
			'x-csrftoken': 'uGeaBdGt8EF51aBV8x1MHP2aizo1Boye',
			'x-ig-app-id': '936619743392459',
			'x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mki7O',
			'x-instagram-ajax': '790551e77c76',
			'x-requested-with': 'XMLHttpRequest'}
		datED = {
			'first_name': name,
			'email': eml,
			'username': user2,
			'phone_number': num,
			'biography': 'By @t.uo',
			'external_url': ext,
			'chaining_enabled': 'on'}
		go2 = r.post(urED,headers=hedED,data=datED)
		if go2.status_code == 200:
			print('Done swap '+user2+'\n\tBy @t.uo')
			input('Press Enter to exit')
			exit(0)
		elif go2.status_code == 400:
			print('The transfer has not been completed !!')
		elif go2.status_code == 429:
			print('The account is blocked')
			exit(0)
def trt():
	global tret,user2
	theards =[]
	for i in range(tret):
		th1 = threading.Thread(target=swap)
		th1.start()
		theards.append(th1)
def yes():
	joker1 = Tk("Warning")
	joker1.config(bg="gray")
	joker1.geometry("0x0+-100+-100")
	messagebox.showinfo('Start','Are you ready ?')
	
# امسح المسج بوكس وخلي الانبوت اذا كنت بتشغل على الجوال
#	input("Are you ready ? [ Enter ]")
	# By JOKER
	trt()

def info():
	global eml,num,bio,name,ext,go,tret,user2
	user2 = input('\nEnter target : ')
	tret = int(input('\nEnter threading : '))
	sis = go.cookies['sessionid']
	urIN = 'https://www.instagram.com/accounts/edit/?__a=1'
	hedIN = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; ds_user_id=45872034997; shbid=6144; csrftoken=uGeaBdGt8EF51aBV8x1MHP2aizo1Boye; rur=RVA; sessionid='+sis,
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'none',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'}
	datIN = {
		'__a': '1'}
	info = r.get(urIN,headers=hedIN,data=datIN)
	name = str(info.json()['form_data']['first_name'])
	ext = str(info.json()['form_data']['external_url'])
	eml = str(info.json()['form_data']['email'])
	bio = str(info.json()['form_data']['biography'])
	num = str(info.json()['form_data']['phone_number'])
	yes()
done=ok
def sc():
	global headLG,go,datLG
	st = go.json()['checkpoint_url']
	coke = go.cookies
	urSC= 'https://www.instagram.com' + st
	g=r.post(urSC,data=datLG,headers=headLG,cookies=coke)
	if ("phone_number") in g.text:
		print("\n 0 >> Phone \n")
	if ("email") in g.text:
		print("\n 1 >> Email \n")
	snd = input(' Enter the type of send : ')
	datSC = {
		"choice": snd}
	go = r.post(urSC,data=datSC,headers=headLG,cookies=coke)
	if ("security_code") in go.text:
		code = input('\n   Enter the security code : ')
		datCO = {
			"security_code": code}
		go = requests.post(urSC,data=datCO,headers=headLG,cookies=coke)
		if ("ok") in go.text:
			coke2 = go.cookies
			print('>> Done login ')
			info()
		else:
			print('\n The security code is invalid !')
def ta():
	global headLG , go , user
	print('  \ntwo factor ')
	st = go.json()['two_factor_info']['two_factor_identifier']
	coke = go.cookies
	cod = input('\n Enter the security code : ')	
	datTA = {
		'username': user,
		'verificationCode': cod,
		'identifier': st,
		'queryParams': '{"next":"/"}'}
	go = r.post('https://www.instagram.com/accounts/login/ajax/two_factor/', headers=headLG,data=datTA,cookies=coke)
	if ("userId") in go.text:
		cookies = go.cookies
		print('>>  Done LoGIN userid')
		info()
	elif ("checkpoint_url") in go.text:
		sc()
	else:
		print('\n The security code is invalid !')
print("""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
	███████ ██     ██  █████  ██████
	██      ██     ██ ██   ██ ██   ██
	███████ ██  █  ██ ███████ ██████
	     ██ ██ ███ ██ ██   ██ ██ ═╦═ ╔══╗
	███████  ███ ███  ██   ██ ██  ║  ║  ╦
	       """+done+"""        ═╩═ ╚══╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def login():
	global headLG , go , datLG , user
	user = input('Enter username : ')
	pess = input('Enter password : ')
	urLG = "https://www.instagram.com/accounts/login/ajax/"
	headLG = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'content-length': '272',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/accounts/login/',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
		'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': '0',
		'x-instagram-ajax': '790551e77c76',
		'x-requested-with': 'XMLHttpRequest'}	
	datLG = {
		"username": user,
		"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{pess}",
		"queryParams": "{}",
		"optIntoOneTap": "false"}
	go = r.post(urLG,headers=headLG,data=datLG)
	if ("userId") in go.text:
		print('\n Done Login \n')
		info()
	elif ("two_factor") in go.text:
		print('\n Binary verification \n')
		ta()
	elif ("checkpoint_url")  in go.text:
		print('\n Account Secure \n')
		sc()
	else:
		print('\nThe username or password is wrong ! \n')
		return login()	
login()
