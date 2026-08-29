# File Integrity Checker

A command-line tool that detects file tampering by comparing SHA-256 hashes 
of files against a saved baseline.

## How it works
1. Scans a folder and computes a SHA-256 hash for every file inside it 
   (including subfolders).
2. Saves those hashes to `baseline.json` as a trusted snapshot.
3. On a later run, re-scans the same folder and compares the new hashes 
   against the baseline — any mismatch means a file was modified, added, 
   or removed since the baseline was created.

## What I learned
- Reading files in chunks (`hashlib` + binary mode) instead of loading 
  everything into memory at once
- Recursing through folder trees with `os.walk()`
- Persisting structured data with `json.dump`/`json.load`
- Catching specific exception types (`FileNotFoundError` vs 
  `json.JSONDecodeError`) instead of a broad catch-all

## Usage
```bash
python main.py
```
Follow the CLI menu to create a baseline, verify a folder against it, 
read the current baseline, or delete it.

## Requirements
No external dependencies — uses only Python's standard library.

---
*Built as part of a series of beginner security/Python projects.*
