#!/usr/bin/env python3
# Author: Maxim3lian

import requests
import os
import re
from multiprocessing.dummy import Pool as ThreadPool
from colorama import init

init(autoreset=True)

# Using a set to store unique results
unique_urls = set()

def ask_dns(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        response = requests.get(f'https://askdns.com/ip/{url}', headers=headers, timeout=30)
        x = response.text  # .text gives string content in Python 3
        if 'Domain Name' in x:
            regex = re.findall('<a href="/domain/(.*?)">', x)
            for domain_name in regex:
                website_url = 'http://' + domain_name
                if website_url not in unique_urls:  # Check for duplicates
                    print(f"GRABBED: {website_url}")
                    unique_urls.add(website_url)  # Add to the set
        else:
            print(f"BAD : {url}")
    except Exception as e:
        print(e)


def rapid_dns(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        response = requests.get(f'https://rapiddns.io/s/{url}?full=1&down=1#result/', headers=headers, timeout=30)
        x = response.text  # .text gives string content in Python 3
        if '<th scope="row ">' in x:
            regex = re.findall('<td>(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}</td>', x)
            for domain_name in regex:
                website_url = 'http://' + domain_name.replace('<td>', '').replace('</td>', '').replace('ftp.', '').replace('images.', '').replace('cpanel.', '').replace('cpcalendars.', '').replace('cpcontacts.', '').replace('webmail.', '').replace('webdisk.', '').replace('hostmaster.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '').replace('autodiscover.', '')
                if website_url not in unique_urls:  # Check for duplicates
                    print(f"GRABBED: {website_url}")
                    unique_urls.add(website_url)  # Add to the set
        else:
            print(f"BAD : {url}")
    except Exception as e:
        print(e)


def reverse_ip_lookup(url):
    try:
        rapid_dns(url)
        ask_dns(url)
    except Exception as e:
        print(e)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        ip_list = input("File Ip : ")  # Use input() for Python 3
        with open(ip_list, 'r') as f:
            urls = f.read().splitlines()
        num_threads = input("Threads : ")  # Use input() for Python 3
        with open('Reversed.txt', 'w') as f:
            for url in unique_urls:
                f.write(url + '\n')
        pool = ThreadPool(int(num_threads))
        pool.map(reverse_ip_lookup, urls)
        
        # Write unique URLs to Reversed.txt
        print("Results saved to Reversed.txt")
        
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
