import dns.resolver
import whois
import time
from datetime import datetime
from datetime import timezone
#Write a get_dns_records(domain) function that returns A, MX, and NS records for a domain
#Write a get_whois_info(domain) function that returns registrar, creation date, expiration date
#Combine both into a single report — print a clean summary for a given domain
#Add a simple heuristic: flag domains registered very recently (e.g. under 30 days old) as "potentially suspicious" — this is a 
# real, common phishing indicator
#rap in a CLI loop like your previous tools, letting the user look up multiple domains
def no_found_domain():
    print("No found domain for the hostname you entered.")
    time.sleep(0.7)

def get_a_record(domain, choice):
    try:
        answer = dns.resolver.resolve(domain, choice)
        for a in answer:
            print(f"IP: {a.to_text()}")
    except (dns.resolver.NoNameservers, dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.LifetimeTimeout):
        no_found_domain()
        return False
    
def get_whois_info(domain):
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
    

def check_gap_domain(domain, creation, thresh_hold=30):
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