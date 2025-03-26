import socket
import requests

def get_reverse_ip_lookup(domain):
    try:
        # Resolve domain to IP
        ip = socket.gethostbyname(domain)
        print(f"Resolved IP for {domain}: {ip}")
    except socket.gaierror:
        print("Error: Domain could not be resolved.")
        return None

    # Query HackerTarget API for reverse IP lookup
    api_url = f"https://api.hackertarget.com/reverseiplookup/?q={ip}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            domains = response.text.splitlines()
            if not domains or "No records" in domains[0]:
                print("No domains found on this server.")
                return []
            return domains
        else:
            print(f"API Error: HTTP {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def main():
    domain = input("Enter the target domain (e.g., bing.com): ").strip()
    domains = get_reverse_ip_lookup(domain)
    
    if domains:
        print(f"\nDomains hosted on the same server as {domain}:")
        for idx, domain in enumerate(domains, 1):
            print(f"{idx}. {domain}")

if __name__ == "__main__":
    main()