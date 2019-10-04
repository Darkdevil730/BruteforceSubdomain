#!/usr/bin/env python
#Mau apa lu?
#Mau Recode
#Inget kalau lu merecode script ini, tidak akan menjadikanmu sebagai seorang mastah
#tinggal pake aja Apa susahnya

import requests
import os
import sys
import multiprocessing

try :
    cgr = "\033[34m"
    cen = "\033[0m"
    cre = "\033[91m"
    
    os.system("sleep 2")
    os.sysem("clear")
    os.system("sleep 2")
    print (cgr +"""                                                                  
 _|_|_|                                            _|             
 _|    _|     _|_|     _|_|_|  _|_|       _|_|_|        _|_|_|    
 _|    _|   _|    _|   _|    _|    _|   _|    _|   _|   _|    _|  
 _|    _|   _|    _|   _|    _|    _|   _|    _|   _|   _|    _|  
 _|_|_|       _|_|     _|    _|    _|     _|_|_|   _|   _|    _|  
                                                                  
                                                                  
SubDomain"""+ cen)
    worldlist=""
    print (cre +"===================================================="+ cgr)
    print (cre +"     Author : D@rk_Devil#666")                     
    print (cre +"       WA   : 089652884613")                       
    print (cre +"      Team  : - Near Cyber Team")
    print (cre +"              - D-Tect Team")                      
    print (cre +"              - CYZ")
    print (cre +"              - Hacker Indonesia")
    print (cre +"              - Dark Defense")                     
    print (cre +"              - ODTM Public")                      
    print (cre +"              - MCTS")                             
    print (cre +"    Github : https://github.com/Darkdevil730")     
    print (cre +"===================================================="+ cgr)
    os.system("sleep 2")
    print ("")
    print (cgr +"[+] Opsi"+ cen)
    print ("1. Bruteforce Subdomain Satan.txt [ 500++ ]")
    print ("0. Exit Proggram")
    print ("")
    memilih = raw_input(cgr +"[?]"+ cen +"Pilih"+ cre +"[1/2]"+ cgr +" : ")
    
    def requests(url):
        try:
            return requests.get("http://"+url)
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.InvalidURL:
            pass
        except UnicodeError:
            pass
        except KeyboardInterrupt:
            print ("[!] Proggram Berhenti")
            sys.exit(0)
        
    if memilih==str("1"):
        worldlist="Satan.txt"
        domain = raw_input(cgr +"[?] Inputkan Domain"+ cre +" : "+ cen)
        requests(domain)
        
    elif memilih==str("0"):
        print (cre +"[√] Terima kasih"+ cen)
        os.system("sleep 2")
        os.system("clear")
        os.system("clear")
        
    else:
        print (cen +"[!] Error : Wrong Input"+ cgr)
        os.system("exit")
    
    with open(worldlist, "r") as worldlist:
        for line in worldlist:
            word = line.strip()
            tes = word+"."+domain
            respon = requests(tes)
            proses = multiprocessing.Process(target=respon, args=(10,20))
            
            if proses:
                print (cgr+"[√]"+cen+"Found >> "+cre+tes+cen)
                
except KeyboardInterrupt:
    print (cgr +"[!] Proggram Berhenti")
    sys.exit(0)