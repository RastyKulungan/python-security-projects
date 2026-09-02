import threading
import socket
import time
from concurrent.futures import ThreadPoolExecutor

def check_port(host, port):# A function to check if a specific port on a host is open. It attempts to create a socket connection to the specified host and port. If the connection is successful, it returns the port number and True; otherwise, it returns the port number and False.
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                return port, result == 0
        except socket.gaierror:
            return port, False
        
def not_digit():# A function to handle the case when the user inputs a non-digit value for the port range. It prints an error message and prompts the user to input digits.
    print("The character you typed is not a digit.")
    time.sleep(0.7)
    print("Input digits.")
    time.sleep(0.7)

if __name__ == '__main__':
    satisfied = False
    KNOWN_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 443: "HTTPS", 3306: "MySQL"
    }
    while not satisfied:
        try:
            ask_port = int(input("What is the range of ports you want to scan?(1 to 100)\n>"))
            ask_port2 = int(input(f"{ask_port} to ?\n>"))
        except ValueError:
            not_digit()
            continue
        ask_host = input("What is your target host?\n>")
        try:
            socket.gethostbyname(ask_host)
        except socket.gaierror:
            print("The hostname you entered cannot be found")
            continue
        start = time.time()
        with ThreadPoolExecutor(max_workers=50) as exec:# A ThreadPoolExecutor is used to manage a pool of threads for concurrent execution. It allows multiple port checks to be performed simultaneously, improving the speed of the port scanning process.
            result = exec.map(lambda port: check_port(ask_host, port), range(ask_port, ask_port2+1))#A lambda function is used to create a simple function that takes a port number and calls the check_port function with the specified host and port. The exec.map method applies this lambda function to each port in the specified range, returning an iterator of results.
            for port, is_open in result:
                if is_open:
                    print(f"{port}:{KNOWN_PORTS.get(port, 'Unknown')} is open")
            end = time.time()
            elapsed = end - start
            print(f"{elapsed:.2f}")
            again = input("Scan again?\n(Y/N)\n>").upper()
            if again == 'N': satisfied = True