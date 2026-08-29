import string
import secrets
from time import sleep

def check_set(sets):

    character_set = []

    if 'p' in sets:
        character_set += string.punctuation
    if 'd' in sets:
        character_set += string.digits
    if 'l' in sets:
        character_set += string.ascii_lowercase
    if 'u' in sets:
        character_set += string.ascii_uppercase
    return character_set

def passwd_generate(length, sets):
    return ''.join(secrets.choice(check_set(sets)) for char in range(length))

if __name__ == '__main__':
    sets = ()
    satisfied = False
    passwd_length = None
    passwd_csets = None
    password = None


    while not satisfied:
        if passwd_length is None:
            try:
                passwd_length = int(input("Enter password length:"))
            except ValueError:
                print("Must be a digit")
                continue
        else:
            print("--Character Sets--")
            print('\n'.join(map(str, ("p", "u", "l", "d"))))
            print("------------------")

            passwd_csets = input("Enter character sets('y' to generate):").lower()
                        
            if passwd_csets == 'y' and len(sets) == 0:
                print("No selected character sets yet.")
                sleep(2)
                continue 
            elif passwd_csets == 'y' and len(sets) >= 1:
                print(f"Password Generated:{passwd_generate(passwd_length, sets)}")
                satisfied = True

            elif len(passwd_csets) > 2:
                print("One character at a time")
                sleep(2)
                continue

            elif passwd_csets not in ("p", "u", "l", "d"):
                print("Character must be in 'sets'!")
                sleep(2)
                continue
            else:
                if passwd_csets in sets:
                    print("Character already selected")
                    continue
                else:
                    temp = list(sets)
                    temp.append(passwd_csets)
                    sets = tuple(temp)
                    print("--Selected Character Sets--")
                    print(' '.join(map(str, sets)))