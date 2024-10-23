import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_ip_from_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return domain, ip
    except socket.gaierror:  # Handle DNS lookup failure
        return domain, "DNS Lookup Failed"
    except socket.error as e:  # Handle other socket errors
        return domain, f"ERROR: {e}"

def main():
    input_file = input('List Domain: ')  # Input file containing domains
    output_file = 'ips.txt'  # Output file for saving IPs

    try:
        with open(input_file, 'r') as file:
            domains = [domain.strip() for domain in file.readlines() if domain.strip()]  # Clean and strip domains
    except FileNotFoundError:
        print(f"ERROR: File '{input_file}' not found.")
        return

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(get_ip_from_domain, domain): domain for domain in domains}
        results = []
        for future in as_completed(futures):
            domain, ip = future.result()
            results.append((domain, ip))

    try:
        with open(output_file, 'w') as file:
            for domain, ip in results:
                file.write(f"{ip}\n")  # Only write the IP address
        print(f"Results saved in {output_file}")
    except IOError as e:
        print(f"ERROR: Unable to write to file '{output_file}': {e}")

if __name__ == "__main__":
    main()
