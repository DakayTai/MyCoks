import os
import requests
from multiprocessing.dummy import Pool as ThreadPool

def check_hahah():
    urls_file = input("List Website # ")
    if not os.path.exists(urls_file):
        print("File not found.")
        return None  # Return None if file not found
    with open(urls_file, 'r', errors='ignore') as fl:
        urls = fl.read().splitlines()
    return urls

def checker_shell(target):
    try:
        response = requests.get(target)
        print(f"Checked {target}")
        if "-rw-r--r" in response.text or "drwxr-xr-x" in response.text:
            with open('aliveshell.txt', 'a') as output_file:
                output_file.write(target + "\n")
                print(f"Shell Alive {target}")# Use target, not urls
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    urls = check_hahah()  # Get URLs from the file
    if urls:  # Ensure urls is not None or empty
        pool = ThreadPool(100)
        pool.map(checker_shell, urls)
        pool.close()  # Close the pool
        pool.join()   # Wait for the worker threads to finish
