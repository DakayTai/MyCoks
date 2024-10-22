import os
import re
import requests
from tqdm import tqdm

def scrape_website(page_type, total_pages=50):
    for page in tqdm(range(0, total_pages), desc=f"Progress {page_type if page_type else 'archive'}"):
        url = f'https://haxor.id/archive/{page_type}?page={page}' if page_type else f'https://haxor.id/archive?page={page}'
        response = requests.get(url)
        html_content = response.text
        pattern = re.compile(r'href=["\'](https?://.*?)["\']')
        matches = pattern.findall(html_content)

        if matches:
            with open('haxor.txt', 'a') as file:
                for href_value in matches:
                    href_value = re.sub(r'^https?://', '', href_value)
                    href_value = re.sub(r'/.*', '', href_value)
                    file.write(f'{href_value}\n')
                    print("Save haxor.txt")

def menu():
    os.system('cls' if os.name == 'nt' else 'clear') 


    TEXT_COLOR = "\033[93m"  
    RESET_COLOR = "\033[0m" 

    print(TEXT_COLOR + '''
       __           ______            __             ___
      / /_  ____  _/_  __/___  ____  / /____   _   _<  /
 __  / / / / / / / // / / __ \/ __ \/ / ___/  | / / / /
/ /_/ / /_/ / /_/ // / / /_/ / /_/ / (__  )   | |/ / /  
\____/\__, /\__,_//_/  \____/\____/_/____/    |___/_/   
     /____/                                          
''' + RESET_COLOR)
    print(TEXT_COLOR + '''
Select the page type to grab:
[1] Special (Haxor.id Site)
[2] Archive (Haxor.id Site)
[0] Exit
''' + RESET_COLOR)

    choice = input("Enter your choice (1, 2, or 0): ")

    if choice == '1':
        print("\nYou selected 'Special' page.")
        scrape_website('special')
    elif choice == '2':
        print("\nYou selected 'Archive' page.")
        scrape_website('')
    elif choice == '0':
        print("Exiting...")
        sys.exit(0)
    elif choice.strip() == "":
        menu() 
    else:
        print("Invalid choice. Please select 1, 2, or 0.")
        menu()  

menu()
