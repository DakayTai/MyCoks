import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

os.system('cls' if os.name == 'nt' else 'clear')

maxix = '\t\t[+] Grabbed : {}'

print('''
[>] DEFACER.NET PRIV8 GRABBER V1.0''')

url_template = 'https://defacer.net/archive/{}'
first_page = int(input('\n\t[>] Enter the first page number: '))
last_page = int(input('\n\t\t[>] Enter the last page number: '))

urls = []
for page in range(first_page, last_page+1):
    
    url = url_template.format(page)

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    
    for text in soup.stripped_strings:
        if '.' in text:
            
            if not text.startswith('http://') and not text.startswith('https://'):
                text = 'http://' + text
            
            parsed_url = urlparse(text)

            domain_name = parsed_url.netloc.split(':')[0]

            domain_parts = domain_name.split('.')
            if len(domain_parts) >= 2:
                tld = domain_parts[-1]
                if len(tld) <= 3:
                    domain_name = '.'.join(domain_parts[-2:])
                else:
                    domain_name = '.'.join(domain_parts[-3:])
            
            if domain_name not in urls:
                urls.append(domain_name)
                print('\n'+maxix.format(domain_name))
    
    with open('defacernet.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')
            print("Save In defacernet.txt")
