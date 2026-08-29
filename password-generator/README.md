# Password Generator

An interactive CLI tool that generates cryptographically secure random 
passwords from user-selected character sets.

## How it works
1. Asks the user for a desired password length.
2. Lets the user pick which character sets to include: punctuation, 
   uppercase, lowercase, digits — one at a time, avoiding duplicates.
3. Generates a random password using only the selected character sets.

## What I learned
- Why `random` is unsafe for security purposes, and why `secrets` uses 
  a cryptographically secure source of randomness instead
- The core `secrets` functions: `choice()`, `randbelow()`, `token_hex()`, 
  `token_urlsafe()`, and `compare_digest()` for timing-safe comparisons
- Passing state explicitly into functions instead of relying on a 
  function silently reading a global variable

## Usage
```bash
python main.py
```
Enter a length, then select character sets (p/u/l/d), then type `y` 
to generate.

## Requirements
No external dependencies — uses only Python's standard library.

---
*Built as part of a series of beginner security/Python projects.*
