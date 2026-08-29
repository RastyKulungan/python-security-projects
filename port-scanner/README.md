# Port Scanner

A concurrent TCP port scanner that checks which ports are open on a 
given host and identifies common services running on them.

## How it works
1. Prompts for a port range and a target host.
2. Validates the hostname resolves before scanning (avoids wasting 
   time/threads on a bad host).
3. Scans the full port range concurrently using a thread pool.
4. Reports open ports along with their commonly associated service 
   (e.g. port 22 = SSH, port 80 = HTTP).
5. Times the scan and reports how long it took.

## What I learned
- TCP sockets: `socket.socket()`, `connect_ex()`, and why `connect_ex` 
  is preferable to `connect()` for scanning (returns an error code 
  instead of raising an exception per attempt)
- The difference between CPU-bound and I/O-bound work, and why 
  threading gives a major speedup for network scanning specifically
- Using `ThreadPoolExecutor` to cap concurrency instead of spawning 
  unlimited raw threads
- Catching `socket.gaierror` for unresolvable hostnames

## ⚠️ Usage note
Only scan hosts you own or have explicit permission to scan. This 
project defaults to testing against `scanme.nmap.org`, a host the 
Nmap project set up specifically for scanner testing.

## Usage
```bash
python main.py
```
Enter a port range and target host when prompted.

## Requirements
No external dependencies — uses only Python's standard library.

---
*Built as part of a series of beginner security/Python projects.*
