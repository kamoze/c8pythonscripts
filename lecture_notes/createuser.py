import os


def new_user():

    confirm = "N"
    while confirm != "Y":
        username = str(input("Enter the name of the user to add:"))
        print("Use the username " + username + " ? (Y/N)")
        confirm = str(input("Input Y or N: ")).upper()
        os.system("sudo adduser " + username)
