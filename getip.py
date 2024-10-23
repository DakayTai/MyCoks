import socket
from multiprocessing.dummy import Pool as ThreadPool  # Use ThreadPool from multiprocessing.dummy

def get_ip_from_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return domain, ip
    except socket.gaierror:  # Handle DNS lookup failure
        pass
    except socket.error as e:  # Handle other socket errors
        pass
    except Exception as e:
        pass

def process_domain(domain):
    result = get_ip_from_domain(domain)
    domain, ip = result
    with open("ips.txt", 'a') as file:  # Append result to file immediately
        file.write(f"{ip}\n")  # Only write the IP address
    return result

def main():
    input_file = input('List Domain: ')  # Input file containing domains

    try:
        with open(input_file, 'r') as file:
            domains = [domain.strip() for domain in file.readlines() if domain.strip()]  # Clean and strip domains
    except FileNotFoundError:
        print(f"ERROR: File '{input_file}' not found.")
        return
    except Exception as e:
        print(f"ERROR: {e}")
        return

    pool = ThreadPool(100)  # Set up the thread pool with 100 threads
    pool.map(process_domain, domains)  # Map the function to the domain list
    pool.close()
    pool.join()  # Close and join the threads

    print(f"Results are being progressively saved to ips.txt.")

if __name__ == "__main__":
    main()
