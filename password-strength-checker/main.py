import string
from english_words import get_english_words_set

def pass_length(password):

    if len(password) >= 8:
        return password
    else:
        return

def pass_variety(password):
    digit = any(char in string.digits for char in password)
    punct = any(char in string.punctuation for char in password)
    letter = any(char in string.ascii_letters for char in password)

    return digit and punct and letter
def pass_complexity(password, common_words):

    return password.lower() not in common_words

def pass_predictability(password):
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

        check_ifokay = 0 #check if functions are true if it is end
        #also if password does not meet requirements reset it to zero

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