import string
from english_words import get_english_words_set #A module to get a set of English words from the 'english-words' package. It is used to check if a password is common or not.

def pass_length(password): # A function to check if the password length is at least 8 characters. If it is, it returns the password; otherwise, it returns None.
    if len(password) >= 8:
        return password
    else:
        return

def pass_variety(password):#A function to check if the password contains at least one digit, one punctuation character, and one letter. It returns True if all conditions are met; otherwise, it returns False.
    digit = any(char in string.digits for char in password)
    punct = any(char in string.punctuation for char in password)
    letter = any(char in string.ascii_letters for char in password)
    return digit and punct and letter

def pass_complexity(password, common_words): # A function to check if the password is not in the set of common words(english_words module). It returns True if the password is not common; otherwise, it returns False.
    return password.lower() not in common_words

def pass_predictability(password):# A function to check if the password does not contain any predictable sequences of characters. It checks for sequences of 4 or more characters from a predefined list of sequences (numbers and letters). If any such sequence is found in the password, it returns False; otherwise, it returns True.
    sequence = ["1234567890", string.ascii_letters]
    for seq in sequence:
        for i in range(len(seq)-3):
            if seq[i:i+4] in password.lower():
                return False
    return True

if __name__ == "__main__":
    common_words = get_english_words_set(['gcide'], lower=True)
    satisfied = False
    while not satisfied:
        check_ifokay = 0 #Checks if the password meets all the criteria. It is incremented for each criterion that the password satisfies. If it reaches 4, it means the password is good.
        password = input("Enter a password:")

        if pass_length(password) is None:
            print("Password is too short")
        else:
            check_ifokay += 1

        if pass_variety(password) is False:
            print("Add uppercase, puncuations and digits")
        else:
            check_ifokay += 1

        if pass_complexity(password, common_words) is False:
            print("Password is common")
        else:
            check_ifokay += 1

        if pass_predictability(password) is False:
            print("Password too predictable")
        else:
            check_ifokay += 1

        if check_ifokay == 4:
            print("Good Password!")
            satisfied = True