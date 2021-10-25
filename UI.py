from colorama import Fore, Back, Style
import os
import time
import socket
from dhooks import Webhook
from platform import *
import datetime
import psutil
import requests
import json




def title():
    os.system('cls & title Aims Community Tool I Beta 1.0')
    print(f'''
                                                {Fore.RED}         Dashboard for{Fore.WHITE}
                                                 ___  ___  _ __ _ __ _____      __
                                                / __|/ _ \| '__| '__/ _ \ \ /\ / /
                                                \__ \ (_) | |  | | | (_) \ V  V / 
                                                |___/\___/|_|  |_|  \___/ \_/\_/  
                                                                                                                                    

                                  
        ''')
    print(f'{Fore.BLACK}[{Fore.RED}~{Fore.BLACK}]{Fore.WHITE}Welcome To Aims Community Tool')            
    print(f'{Fore.BLACK}[{Fore.RED}~{Fore.BLACK}]{Fore.WHITE}Login')
    print(f'{Fore.BLACK}[{Fore.RED}~{Fore.BLACK}]{Fore.WHITE}Register')
    print(f'{Fore.BLACK}[{Fore.RED}~{Fore.BLACK}]{Fore.WHITE}Information')
    print(f'{Fore.BLACK}[{Fore.RED}~{Fore.BLACK}]{Fore.WHITE}Commands')

    opt = input(f'{Fore.BLACK}[{Fore.RED}~{Fore.BLACK}]{Fore.RED}$~ {Fore.WHITE}')

    if opt == "1":
        options()



def options():
    print(f'''{Fore.RED}
    [+]═══════════════════════════════════════[+]
     ║  {Fore.WHITE}1{Fore.RED}~           {Fore.WHITE}6{Fore.RED}~           {Fore.WHITE}11{Fore.RED}~          ║
     ║  {Fore.WHITE}2{Fore.RED}~           {Fore.WHITE}7{Fore.RED}~           {Fore.WHITE}12{Fore.RED}~          ║
     ║  {Fore.WHITE}3{Fore.RED}~           {Fore.WHITE}8{Fore.RED}~           {Fore.WHITE}12{Fore.RED}~          ║    
     ║  {Fore.WHITE}4{Fore.RED}~           {Fore.WHITE}9{Fore.RED}~           {Fore.WHITE}14{Fore.RED}~          ║
     ║  {Fore.WHITE}5{Fore.RED}~           {Fore.WHITE}10{Fore.RED}~          {Fore.WHITE}15{Fore.RED}~          ║
     ║                                         ║
     ║                                         ║
     ║                                         ║
     ║                                         ║
    [+]═══════════════════════════════════════[+]
    
    ''')
    time.sleep(100000)



def settings():
    print(f'{Fore.RED}[+]═══════════════════════════════════════[+]')
    print(f'')










title()


