#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Author: Thiago (THX)
# Github: github.com/thxsena
# How to use: python byadmin.py http://www.site.com wordlist.txt
#
#  _____     _____   _       _     
# | __  |_ _|  _  |_| |_____|_|___ 
# | __ -| | |     | . |     | |   |
# |_____|_  |__|__|___|_|_|_|_|_|_|
#       |___|Created by Thiago(THX)  
#--------------------------------------


import requests
import sys

def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))

prGreen('''

 _____     _____   _       _     
| __  |_ _|  _  |_| |_____|_|___ 
| __ -| | |     | . |     | |   |
|_____|_  |__|__|___|_|_|_|_|_|_|
      |___|Created by Thiago(THX)                     

''')
print""

host = sys.argv[1]

#open a file
word = open(sys.argv[2],'r')

#retorna a lista contendo as linhas
lines = word.readlines()

#close opend file
word.close()

for line in lines:
	line = line.replace("\n","")
	pwn = host+"/"+line
	pwned = pwn
	r = requests.get(pwned)
	stat = r.status_code
	if stat == 200:
		print '\033[31m'+"[+]"+"\033[0;0m"+"URL FOUND: "+pwn
	else:
		print "[-] URL NOT FOUND: "+pwn
