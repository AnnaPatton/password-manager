# importing module that enables encryption
from cryptography.fernet import Fernet

# define key - takes text string then converts to random text. unencryption can occur if user has key + password
# function that creates key - if you have the key, you can comment this function out
'''
def write_key():
    key = Fernet.generate_key()

    # opens a file (named key.key) in WriteBytes format
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''

# function that retrieves key
# opens file in Read/Bytes mode, reads the file, closes file, returns key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)
    
# create functions for view and add
def view():
    
# 3 modes = w (overrides/replaces old files and erases existing data), r (read-mode only), a (allows user to add to end of existing file, read file, or create new file)
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            # data.split("|") looks for the character then it'll split = allowing us to split name and password
            user, passw = data.split("|")
            # decrypt the passwords for viewing mode; decode will convert bytes str to regular str
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

# create a new file (if the file doesn't already exist) then add password into it
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")


# "with" keyword = after done with operations in file, will auto close file; could manually open/close file but causes interferences
    with open("passwords.txt", "a") as f:
# accepts name and pwd, separates with pwd, with line break; converted the password to encrypted version
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# option: add or view passwords
while True:
    mode = input("Would you like to view existing passwords or add a new password (type view or add)?, press q to quit ").lower()

    # if user quits, break the while loop
    if mode == "q":
        break

    # calling the view and add functions - depending on what mode is selected, the function being called will be run
    elif mode == "view":
        view()

    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        # continue will bring user back to the while loop
        continue