# Security Header Checker

A CLI tool that checks whether a website returns important HTTP 
security headers, and flags headers that leak information which could 
make a site more vulnerable to attack.

## How it works
1. Prompts for a URL to check.
2. Sends a `GET` request (5 second timeout) and retrieves the response 
   headers.
3. Compares the returned headers against a list of expected security 
   headers (e.g. `Content-Security-Policy`, `X-Frame-Options`) and 
   prints a score showing how many were found.
4. Checks for "vulnerable" headers (e.g. `Server`) that reveal 
   information useful to an attacker, and prints a warning if found.
5. Loops, letting you check additional URLs until you choose to stop.

## What I learned
- Handling different `requests` exception types (`ConnectionError`, 
  `Timeout`, `MissingSchema`, `InvalidURL`) separately so the program 
  fails gracefully instead of crashing
- Iterating over response headers and checking membership against a 
  tuple of expected values
- Structuring a simple loop-driven CLI with a clean exit condition
- Why some HTTP headers matter for security, and what it means when 
  they're missing or when a header leaks server information

## Usage
```bash
python security_header_checker.py
```
Enter a URL (including `http://` or `https://`) when prompted.

## Requirements
requests

Install with: `pip install requests`

---
*Built as part of a series of beginner security/Python projects.*