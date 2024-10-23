import socket
from concurrent.futures import ThreadPoolExecutor

def get_ip_from_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return domain, ip
    except socket.error as e:
        return domain, f"ERROR: {e}"

def main():
    input_file = input('List Domain: ')  # Nama file input yang berisi daftar domain
    output_file = 'ips.txt'               # Nama file output untuk menyimpan IP

    with open(input_file, 'r') as file:
        domains = [domain.strip() for domain in file.readlines() if domain.strip()]  # Menghapus spasi dan newline

    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(get_ip_from_domain, domains))

    with open(output_file, 'w') as file:
        for domain, ip in results:
            file.write(f"{domain} => {ip}\n")

    print("Save In ips.txt")

if __name__ == "__main__":
    main()
