# Password Strength Checker

A command-line tool that evaluates a password against several security 
criteria and reports whether it's strong enough.

## How it works
1. Prompts the user for a password.
2. Checks it against four criteria:
   - **Length** — at least 8 characters
   - **Variety** — contains a mix of letters, digits, and punctuation
   - **Complexity** — isn't a common English dictionary word
   - **Predictability** — doesn't contain an obvious sequential run 
     (e.g. "1234" or "abcd")
3. Loops until the password passes all four checks, telling the user 
   exactly what's missing along the way.

## What I learned
- The difference between checking "does at least one character match" 
  vs. "do all required categories exist" using `any()`
- Why returning inside a loop can silently skip checking the rest of 
  the data (an early-return bug I hit more than once)
- Comparing a string against a dictionary/set of common words rather 
  than comparing individual characters to it

## Usage
```bash
python main.py
```
Enter a password when prompted. The tool will tell you what to fix 
until your password passes all checks.

## Requirements
english-words
Install with: `pip install english_words`

---
*Built as part of a series of beginner security/Python projects.*
