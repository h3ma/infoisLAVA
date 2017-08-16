#!/usr/bin/python
# coding=utf-8

import json
import os
import sys
import getopt
import socket
import re
import requests
import urlparse
import time
import urllib
import shodan
from urllib2 import *

# list = ["ping", "request", "whois", "ip", "email gathering"]
api_key = "https://api.shodan.io/shodan/host/{ip}?key={0fTS2YJPZAOSQHnC7kSEI06LrTg7pPcV}"
src = "https://api.shodan.io/shodan/host/search?key={0fTS2YJPZAOSQHnC7kSEI06LrTg7pPcV}&query={ip}&facets={facets}"


class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'


os.system("clear")
banner1 = bcolors.BLUE + bcolors.BOLD + """ 
                  /|\ 
                /  |  \ 
              /   '|   '\ 
              |    |    | 
              |    |    | 
              |    |    | 
              |    |    | 
              |    |    | 
              |    |    | 
              |    |    | 
              |    |    | 
              |    |    | 
              | .·´|`·. | 
              |;::;|;::;| 
              |;::;|;::;| 
              |;::;|;::;| 
              |;::;|;::;| 
              | .·´¯`·. | 
              |;       ;| 
              |'`·._.·´'| 
              |;::;|;::;| 
      |¯`·._.·´¯¯¯¯¯¯¯¯¯`·._.·´¯| 
      |                        '| 
      |.·´¯`·.___HEMA__ '.·´¯`·.| 
      |.·´¯`·.___     '___.·´¯`·.| 
             .·´      `·.     
             |.·´¯`·..·´| 
             |`·._.·´`·.| 
             |.·´¯`·..·´| 
             |`·._.·´`·.| 
             |.·´¯`·..·´| 
             `·.      .·´ 
            . · ´¯¯¯¯` · .   
       ,  ' ,'  .·´¯`·.   ', ', 
         ', ',  `·._.·´  ,' ,' 
            '  ,_____,  ' 
               `·..·´  instagram :: h3ma__ """
print banner1
print bcolors.GREEN + "please be patient"
time.sleep(.300)
print bcolors.YELLOW + bcolors.BOLD + "\t\t\tcongrats u waited 3 sec\n\n"
print bcolors.RED + "[+]" + bcolors.RED + "ping \t\tping a host or a domain"
print bcolors.BLUE + "[+]" + bcolors.BLUE + "web scanner \t\tscan ports for a web or a domain"
print bcolors.GREEN + "[+]" + bcolors.GREEN + "emailG \t\tgathering emails from domains or servers"
print bcolors.YELLOW + "[+]" + bcolors.YELLOW + "webG \t\tgathering infos about a web"
print bcolors.RED + "[+]" + bcolors.RED + "scanMY \t\tscanning your host or your clients on your router"
choice = "LAVA:> "
list1 = raw_input(bcolors.BOLD + bcolors.GREEN + choice)
if list1 == 'ping':
    hostname = raw_input(bcolors.YELLOW + bcolors.BOLD + "the servers ip u want: " + bcolors.GREEN)
    os.system("ping " + hostname)
elif list1 == 'request':
    os.system("clear")
    #    api = "UNmOjxeFS2mPA3kmzm1sZwC0XjaTTksy"
    req1 = raw_input("your request: ")
    x = urllib.urlopen("https://www.shodan.io/search?query=" + req1)
    #    data = json.load(x)
    print x.read()
    print "\n\n"
# print data
# elif list1 == 'shodan':
#    y = urllib.urlopen(src)
#    encoded = urllib.quote(src)
#    z = json.load(y)
#    print encoded
elif list1 == 'web scanner':
    print "just type the website "
    web = raw_input(bcolors.FAIL + "the domain: ")
    os.system("nmap -T4 -A -v " + web)
elif list1 == 'webG':
    domip = raw_input('\033[1;91mEnter Domain or IP Address: \033[1;m')
    who = "http://api.hackertarget.com/whois/?q=" + domip
    pwho = urlopen(who).read()
    print (pwho)
elif list1 == 'emailG':
    os.system("clear")
    q = raw_input(bcolors.BLUE + "enter the domain or the ip:" + bcolors.RED)
    os.system("theharvester" + " -d " + q + " -b " + "google")
elif list1 == 'scanMY':
    os.system("route -n")
    print "which one is your ip gateway is\n192.168.1.1 type 1 \n192.168.0.1 type 2"
    gateway = raw_input("route:>")
    if gateway == '1':
        os.system("nmap -T4 -A -v 192.168.1.*" + bcolors.BLUE)
    elif gateway == '2':
        os.system("nmap -T4 -A -v 192.168.0.*")
    else:
        print bcolors.FAIL + "something went wrong"
else:
    print bcolors.FAIL + "make sure u type them right!!!!!"
