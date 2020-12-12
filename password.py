# password generator
import random
import string
import hashlib
from pyfiglet import Figlet

strt = True
while strt:
    print("""
   \u001b[36m -------------------------------------------
   \u001b[36m |   \u001b[31m 1. Password Generator  \u001b[36m              |
   \u001b[36m |   \u001b[31m 2. Password Hasher (sha256) \u001b[36m         |
   \u001b[36m |   \u001b[31m 3. Exit \u001b[36m                             |         
   \u001b[36m -------------------------------------------
    """)
    strt = input("select option: ")
    if strt == "1":
        welcome_pw = Figlet(font="big")
        print(welcome_pw.renderText(" password  generator"))
        pw_length = int(input("\u001b[31m how many characters do you want the password to contain?: \u001b[36m"))

        characters = string.ascii_letters + string.digits + string.punctuation

        password = []

        for x in range(pw_length):
            password.append(random.choice(characters))
        print("password is:")
        print(''.join(password))

    # HASHER
    elif strt == "2":
        x = input("Enter What You Want To Hash: ")
        hash_object = hashlib.sha256(x.encode())
        hex_dig = hash_object.hexdigest()
        print("\u001b[31mOriginal hash     : ", hex_dig)
        print("Every 9 characters: ", hex_dig[::5])

    elif strt == "3":
        break

    elif strt != "":
        print(" please select valid number")
