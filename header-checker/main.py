import requests

def get_headers(url):#This function gets the url with a timeout of 5 seconds. Will return None if the requests failed.
    try:
        result = requests.get(url, timeout=5)
        return result.headers
    except requests.exceptions.ConnectionError:
        print("Connection error occurred. Please check the URL and try again.")
        return
    except requests.exceptions.Timeout:
        print("Request timed out.")
        return
    except requests.exceptions.MissingSchema:
        print("Invalid URL schema.")
        return
    except requests.exceptions.InvalidURL:
        print("Invalid URL.")
        return

def check_security_headers(headers, security_header, vulnerable):#This function gets the header with what the get_header functions returns then appends it to a list to check if how many headers it has.
    in_header = []
    for header in headers:
        if header in security_header:
            in_header.append(header)
        if header in vulnerable:
            print("Warning: Vulnerable header found: " + header)
    return in_header
    
if __name__ == '__main__':
    headers = ("X-Content-Type-Options", "Strict-Transport-Security",   #The headers that the program checks for add more if #you know more headers.
               "X-Frame-Options", "Content-Security-Policy", "Content-Security-Policy-Report-Only") 
    vulnerable_header = ("Server",)   #Vulnerable headers that make the website weak.      
    running = True         

    while running:
        score = 0    
        enter_url = input("Enter url:\n")              
        header_host = get_headers(enter_url)
        if header_host is not None:
            try:
                header_present = check_security_headers(header_host, headers, vulnerable_header)
                score = len(header_present)
            except TypeError:
                print("Function returned none.")
            print(f"Score: {score}/{len(headers)}")
            for header in header_present:
                print(f"Header found: {header}")
            run_again = input("Do you want to check another url? (y/n):\n")
            if run_again.lower() != 'y':
                running = False
        else:
            continue