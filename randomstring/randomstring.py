# Programmed by @OfficialJavaScript on GitHub

import random

lalphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ualphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special_characters = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', ';', ':', '"', '\'', ',', '.', '<', '>', '?', '/']

def letterstr(length):
    if not length:
        return ("Define length")
    if not str(length).isdigit():
        return ("Numbers only, no speechmarks or commas!")
    password = ""
    length = (length)
    for _ in range(int(length)):
        password += random.choice(lalphabet + ualphabet)
    return password
            
def numberstr(length):
    if not length:
        return ("Define length")
    if not str(length).isdigit():
        return ("Numbers only, no speechmarks or commas!")
    password = ""
    length = int(length)
    for _ in range(int(length)):
        password += random.choice(numbers)
    return password

def abcspecialcharstr(length):
    if not length:
        return ("Define length")
    if not str(int(length)).isdigit():
        return ("Numbers only, no speechmarks or commas!")
    password = ""
    for _ in range(length):
        choice = random.randint(1, 4)
        if choice == 1:
            password += random.choice(lalphabet + ualphabet)
        elif choice == 2:
            password += random.choice(numbers)
        elif choice == 3:
            password += random.choice(special_characters)
        else:
            password += random.choice(lalphabet + ualphabet + numbers + special_characters)
    return password

def randomstr(length):
    if not length:
        return ("Please define the length.")
    if not str(int(length)).isdigit():
        return ("{length} is not a number.")
    password = ""
    for _ in range(int(length)):
        choice = random.choice([1, 2, 3, 4])
        if choice == 1:
            password = f"{password}{random.choice(lalphabet)}"
        if choice == 2:
            password = f"{password}{random.choice(ualphabet)}"
        if choice == 3:
            password = f"{password}{random.choice(numbers)}"
        if choice == 4:
            password = f"{password}{random.choice(special_characters)}"
    return password

if __name__ == "__main__": # Wm5xciBvbCBAQnNzdnB2bnlXbmluRnBldmNn
    print("This is script is designed to be imported, but can be ran this way if wanted.")