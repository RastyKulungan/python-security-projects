import dns.resolver
import whois
import time
from datetime import datetime
from datetime import timezone

def no_found_domain():
    print("No found domain for the hostname you entered.") #A statement to be printed when the domain is not found.
    time.sleep(0.7)

def get_a_record(domain, choice): # A function to get the specified record of a domain.
    try:
        answer = dns.resolver.resolve(domain, choice)
        for a in answer:
            print(f"IP: {a.to_text()}")
    except (dns.resolver.NoNameservers, dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.LifetimeTimeout):
        no_found_domain()
        return False
    
def get_whois_info(domain): # A function to get the whois information of a domain.
    try:
        info = whois.whois(domain)
        if info.domain_name is None:
            print("No found domain with the hostname you entered.")
            return
        else:
            creation = info.creation_date
            expiration = info.expiration_date
            print(f"Registrar: {info.registrar}")
            if isinstance(creation, list):
                creation = creation[0]
            check_gap_domain(domain, creation)
            print(creation)
            if isinstance(expiration, list):
                expiration = expiration[0]
            print(expiration)
    except Exception as e:
        print(f"Look up failed {e}")
    

def check_gap_domain(domain, creation, thresh_hold=30): # A function to check the gap between the current date and the creation date of a domain.
    since_created = (datetime.now(timezone.utc) - creation).days
    if since_created < thresh_hold:
        print("Domain created recently!\nPotentially a phishing website!")  
    else:
        print(f"{since_created:,}Days")  
    
if __name__ == "__main__":
    satisfied = False
    while not satisfied:
        record = input("Enter record.\n(A, MX, NS)\n>").lower()
        if record not in ("a", "mx", "ns"):
            print("The text you entered is not within the option.")
            time.sleep(0.7)
            continue
        hostname = input("Enter hostname.\n>")
        if get_a_record(hostname, record) is False:
            continue
        else:
            get_whois_info(hostname)
            ask = input("Enter character (Y) to scan another domain.\n>").upper()
            if ask != 'Y': satisfied = True