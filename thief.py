import webbrowser
import requests
import time
import os
import colorama
import json
from io import StringIO
if os.name == 'nt':
    from colorama import init
    init(convert=True)
    os.system('title Thief - Coded By: vx#1234')
key1 = '' 
uid1 = ''
key2 = ''
uid2 = ''
uid3 = ''
key3 = '' #Logins for blist api script, create some at https://www.neutrinoapi.com/
key4 = ''
uid4 = ''
key5 = ''
uid5 = ''
def logo():
    clear()
    print("""
      /###           /  /                         /##
     /  ############/ #/        #               #/ ###
    /     #########   ##       ###             ##   ###
    #     /  #        ##        #              ##
    ##  /  ##        ##                       ##
        /  ###        ##  /## ###       /##    ######
       ##   ##        ## / ### ###     / ###   #####
      ##   ##        ##/   ### ##    /   ###  ##
       ##   ##        ##     ## ##   ##    ### ##
       ##   ##        ##     ## ##   ########  ##
        ##  ##        ##     ## ##   #######   ##
         ## #      /  ##     ## ##   ##        ##
         ###     /   ##     ## ##   ####    / ##
           ######/    ##     ## ### / ######/  ##
            ###       ##    ##  ##/   #####    ##
                            /
                           /
                          /
                         /
    """)

def main():
    logo()
    print("""

                Fake VCC Generation Tool
          (don't use this tool without a vpn)
          -------------------------------------
            blist - large list of working bins
            blookup - Lookup a bin and retrieve info on it
            gen - generate vccs in bulk
            check - check validity of vccs (put cards cc.txt)
            exit - exit the program
          -------------------------------------
    """)

    cmd = input("Mode: ")
    if cmd == 'blist':
        binlist()
    elif cmd == 'blookup':
        attempt1()
        main()
    elif cmd == 'gen':
        webbrowser.open('https://namso-gen.com/')
        main()
    elif cmd == 'check':
        checker()
    elif cmd == 'exit':
        exit
    else:
        print("[X] Invalid Command!")
        time.sleep(3)
        main()
def checker():
    open_file = open('cc.txt', 'r').readlines()
    Live = open('Live.txt', 'a')
    try:
        for i in open_file:
            Card = i.strip()
            url = 'https://gostrafx.com/api.php'
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
                'Content-Length': '38',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': '__cfduid=d2c88b57c174ff05f28702c80dadf37d31619222046; _ga=GA1.2.197023261.1619222048; _gid=GA1.2.1208491135.1619222048; _gat_gtag_UA_162747950_1=1',
                'Host': 'gostrafx.com',
                'Origin': 'https://gostrafx.com',
                'Referer': 'https://gostrafx.com/cc-checker/index.php',
                'TE': 'Trailers',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
                'X-Requested-With': 'XMLHttpRequest'
            }
            data = {
                'data': Card
            }
            r = requests.post(url, headers=headers, data=data)
            if '"error":4' in r.text:
                print("> Invalid Format : " + Card)
            elif '"error":2' in r.text:
                print("> Die : " + Card)
            elif '"error":3' in r.text:
                print("> Error : " + Card)
            elif '"error":1' in r.text:
                print('> Live : ' + Card)
                Live.write(Card + "\n")
            else:
                Live.write(Card + "\n") # attempt to write ccs anyway
                print("> Something Went Wrong Contact @MHMY")
                time.sleep(3)
                main()
    except:
        Live.write(Card + "\n") #attempt to write ccs if sesh ended early
        print("Session Ended!")
        time.sleep(3)
        main()
    main()
# binlookup loop
def attempt1():
    logo()
    print("""
    NeutrinoAPI Fallback Script
        Coded by: vx#1234
    """)
    bin = input('BIN: ')
    url = 'https://neutrinoapi.net/bin-lookup'

    data = {
        'api-name': 'bin-lookup',
        'bin-number': bin,
        'customer-ip':  '',
        'api-key': key1,
        'user-id': uid1,
    }
    response = requests.post(url, data=data).text
    print(response)
    if response == '{"api-error":2,"api-error-msg":"DAILY API LIMIT EXCEEDED"}':
        clear()
        print("Account Limited, Attempting Lookup with Different Account. Switch IPs & Press Any Key to Continue")
        key = input("> ")
        if key == 'a':
            attempt2()
        else:
            attempt2()
    elif response == '{"api-error":4,"api-error-msg":"ACCOUNT OR IP BANNED"}':
        clear()
        print("Your Account or IP has been banned. Check Account Status and Change IP")
        time.sleep(5)
        main()
    else:
        print("Lookup Complete, Press Any Key To Continue.")
        key = input("> ")
        if key == 'a':
            main()
def attempt2():
    logo()
    print("""
    NeutrinoAPI Fallback Script
        Coded by: vx#1234
    """)
    bin = input('BIN: ')
    url = 'https://neutrinoapi.net/bin-lookup'

    data = {
        'api-name': 'bin-lookup',
        'bin-number': bin,
        'customer-ip':  '',
        'api-key': key2,
        'user-id': uid2,
    }
    response = requests.post(url, data=data).text
    print(response)
    if response == '{"api-error":2,"api-error-msg":"DAILY API LIMIT EXCEEDED"}':
        clear()
        print("Account Limited, Attempting Lookup with Different Account. Switch IPs & Press Any Key to Continue")
        key = input("> ")
        if key == 'a':
            attempt3()
        else:
            attempt3()
    elif response == '{"api-error":4,"api-error-msg":"ACCOUNT OR IP BANNED"}':
        clear()
        print("Your Account or IP has been banned. Check Account Status and Change IP")
        time.sleep(5)
        main()
    else:
        print("Lookup Complete, Press Any Key To Continue.")
        key = input("> ")
        if key == 'a':
            main()
def attempt3():
    logo()
    print("""
    NeutrinoAPI Fallback Script
        Coded by: vx#1234
    """)
    bin = input('BIN: ')
    url = 'https://neutrinoapi.net/bin-lookup'

    data = {
        'api-name': 'bin-lookup',
        'bin-number': bin,
        'customer-ip':  '',
        'api-key': key3,
        'user-id': uid3,
    }
    response = requests.post(url, data=data).text
    print(response)
    if response == '{"api-error":2,"api-error-msg":"DAILY API LIMIT EXCEEDED"}':
        clear()
        print("damn nigga, you limited all your accounts? why you looking up so much bins lmao")
        key = input("> ")
        if key == 'a':
            attempt2()
        else:
            attempt2()
    elif response == '{"api-error":4,"api-error-msg":"ACCOUNT OR IP BANNED"}':
        clear()
        print("Your Account or IP has been banned. Check Account Status and Change IP")
        time.sleep(5)
        main()
    else:
        print("Lookup Complete, Press Any Key To Continue.")
        key = input("> ")
        if key == 'a':
            main()
#end binlookup loop
def binlist():
    logo()
    response = requests.get('https://pastebin.com/raw/eqzBiLjN').text
    print(response)
    print("Press Any Key To Return To Main Menu")
    key = input('> ')
    if key == 1:
        main()
    else:
        main()
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



main()
