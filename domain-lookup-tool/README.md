# Domain Lookup Tool

A CLI tool that looks up DNS records and WHOIS registration info for a 
domain, and flags recently-registered domains as a potential phishing 
indicator.

## How it works
1. Prompts for a DNS record type (A, MX, or NS) and a target domain.
2. Resolves and prints the requested DNS record(s).
3. Fetches WHOIS info: registrar, creation date, expiration date.
4. Calculates how many days ago the domain was registered — domains 
   under 30 days old are flagged as potentially suspicious, since 
   attackers commonly register fresh domains for short-lived phishing 
   campaigns.

## What I learned
- Querying DNS records with `dns.resolver`, and handling the different 
  exception types (`NXDOMAIN`, `NoAnswer`, `NoNameservers`) separately
- Working with WHOIS data via the `whois` library, including handling 
  inconsistent return types (a single `datetime` vs. a list of them) 
  using `isinstance()`
- Timezone-aware vs. naive `datetime` objects, and why subtracting 
  mismatched ones raises an error
- Avoiding redundant network calls by fetching data once and reusing 
  it, rather than calling the same lookup function multiple times

## Usage
```bash
python main.py
```
Enter a record type (a/mx/ns) and a domain when prompted.

## Requirements
dnspython
python-whois

Install with: `pip install dnspython python-whois`

---
*Built as part of a series of beginner security/Python projects.*
