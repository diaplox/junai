#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from junaiv1 import *
from junaiv2 import *

os.system("clear")
print ga.green+'''

\033[1;96m██╗    ██╗███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
\033[1;95m██║    ██║██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
\033[1;94m██║ █╗ ██║█████╗  ██████╔╝███████╗██║     ███████║██╔██╗ ██║
\033[1;93m██║███╗██║██╔══╝  ██╔══██╗╚════██║██║     ██╔══██║██║╚██╗██║
\033[1;92m╚███╔███╔╝███████╗██████╔╝███████║╚██████╗██║  ██║██║ ╚████║
\033[1;91m╚══╝╚══╝ ╚══════╝╚═════╝ ╚══════╝╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
\033[1;97m********************************************************************* 
\033[1;93m*   created:[+]\033[1;92mNOVOHORY - NOVOSAD                                    
\033[1;92m*   github:[+]\033[1;95mNot responsible for your actions
\033[1;92m*   Instagram:[+]\033[1;95mhttps://Instagram.com/NOVOHORY
*********************************************************************                                                 
            
           🇹🇭🇮🇸 🇹🇴🇴🇱 🇨🇷🇪🇦🇹🇪🇩 🇧🇾 Junai - pqqqf  
            
\033[1;91m*This tools is very easy to use, and dont use this tools to scan 
\033[1;91m*for anyone website without their permission as i wont be        
\033[1;91m*responsible for any harm done with this tools.                  
\033[1;91m*This tools is very easy and simple to use.                          
        '''+ga.end

def urls_or_list():
    url_or_list = raw_input(" \033[1;92m[!] Scan URL or List of URLs? [1/2]: ")
    if url_or_list == "1":
        url = raw_input(" [!] Enter the URL: ")
        if "?" in url:
            rce_func(url)
            xss_func(url)
            error_based_sqli_func(url)
        else:
            print ga.red + "\n [Warning] " + ga.end + ga.bold + "%s" % url + ga.end + ga.red + " is not a valid URL" + ga.end
            print ga.red + " [Warning] You should write a Full URL with a query string. e.g. http://site.com/page?id=value \n" + ga.end
            os.system('xdg-open https://Instagram.com/pentasec/')
            exit()
    elif url_or_list == "2":
        urls_list = raw_input(ga.green + " [!] Enter the list file name .e.g [list.txt]: " + ga.end)
        open_list = open(urls_list).readlines()
        for line in open_list:
            if "?" in line:
                links = line.strip()
                url = links
                print ga.green + " \n [!] Now Scanning %s" % url + ga.end
                rce_func(url)
                xss_func(url)
                error_based_sqli_func(url)
            else:
                links = line.strip()
                url = links
                print ga.red + "\n [Warning] " + ga.end + ga.bold + "%s" % url + ga.end + ga.red + " is not a valid URL" + ga.end
                print ga.red + " [Warning] You should write a Full URL with a query string. e.g. http://site.com/page?id=value \n" + ga.end
        exit()

urls_or_list()
