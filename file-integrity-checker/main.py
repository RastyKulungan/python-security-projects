import hashlib
import json
import os
from time import sleep

def abort(): # A function to abort the program.
    print("Aborting", end='')
    for time in range(3):
        sleep(0.8)
        print(".", end="")
    return

def file_not_found():# A function to print a message when the file or folder is not found.
    print("\nPath does not exist")
    sleep(0.8)
    print("Terminating")
    sleep(0.8)
    return

def hash_file(file_path): # A function to hash a file into chunks (4096 bytes) using SHA-256 algorithm.
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        chunk = f.read(4096)
        while chunk:
            hasher.update(chunk)
            chunk = f.read(4096)
    return hasher.hexdigest()
            
def hash_folder(folder_path): # A function to hash all files in a folder and return a dictionary of file paths and their corresponding hashes.
    hash = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full = os.path.join(root, file)
            hash[full] = hash_file(full)
    if hash == {}:
        file_not_found()
        return
    else:
        return hash

def save_data(data): # A function to save the hashed data into a JSON file named "baseline.json". If the file already exists, it will not overwrite it.
    if data == None:
        return
    else:
        try:
            with open("baseline.json", 'r') as j:
                js = json.load(j)
        except (FileNotFoundError, json.JSONDecodeError):
            js = None
        if js is not None:
            print("Cant create another baseline because it already exist")
            return
        else:
            print("Baseline created!")
            sleep(0.8)
            with open("baseline.json", "w")as j:
                js = json.dump(data, j, indent=4)

def load_data(): # A function to load the hashed data from the JSON file named "baseline.json" and print it. If the file does not exist, it will print a message.
    try:
        with open("baseline.json", 'r') as j:
            js = json.load(j)
            for file, hash in js.items():
                print(f"{file} : {hash}") 
    except (FileNotFoundError, json.JSONDecodeError):
        file_not_found()

def verify_file(baseline, folder_path): # A function to verify the integrity of a folder by comparing its current hash with the baseline hash stored in the JSON file named "baseline.json". If the hashes do not match, it will print a warning message.
    hashing = hash_folder(folder_path)
    try:
        with open(baseline, "r") as j:
            js = json.load(j)
    except (FileNotFoundError, json.JSONDecodeError):
        return
    else:
        if hashing is None:
            return
        elif js != hashing:
            print("\nWARNING:Folder has been tampered!")
            return True
        else:
            return False

def delete_baseline(baseline_path): # A function to delete the baseline JSON file named "baseline.json". If the file does not exist, it will print a message.
    try:
        os.remove(baseline_path)
    except FileNotFoundError:
        print("File does not exist, or maybe a wrong path?")
        sleep(0.8)

if __name__ == '__main__':
    satisfied = False

    while not satisfied:
        cli = input("\n----------HASH CHECKER----------\n"
                    "1. Create baseline\n"
                    "2. Verify baseline\n"
                    "3. Read baseline\n"
                    "4. Delete baseline\n"
                    "5. Exit\n"
                    "-------------------------------\n"
                    ">")
        
        if cli not in "12345" or len(cli) > 1:
            print("Not a valid choice~")
            for text in range(3):
                print(".", end='')
                sleep(0.8)
            continue
        match(cli):
            case '1':
                cli1 = input("Do you want to create a baseline for saving data?\n(Y/N)\n>").upper()
                if cli1 == 'Y':
                    path = input('Enter folder path "/path/to/folder"\n>')
                    save_data(hash_folder(path))
                else:
                    abort()
                    continue
            case '2':
                verify1 = input('Enter path to the folder you want to verify "/path/to/folder"\n>')
                print("Verifying", end='')
                for time in range(3):
                    sleep(0.8)
                    print(".", end='')
                if verify_file("baseline.json", verify1) == False:
                    print("\nFolder has not been tampered.")
                    sleep(0.8)
            case '3':
                load_data()
            case '4':
                delete = input('Delete current baseline?"\n(Y/N)\n>').upper()
                if delete == 'Y':
                    print("Deleting", end='')
                    for time in range(3):
                        sleep(0.5)
                        print(".", end="")
                    delete_baseline("baseline.json")
                else:
                    abort()
                    continue
            case '5':
                abort()
                satisfied = True