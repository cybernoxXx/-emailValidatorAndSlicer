import re

regex = r'^[a-zA-A0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def emailcheck(email):
    if re.fullmatch(regex, email):
        print("You provide a valid email")
    else:
        print("You provide a non valid email")


while True:
    email = input("Insert a valid email: ")
    emailcheck(email)

    slice = email.split("@")

    print(f"The username is {slice[0]} and the domain is {slice[1]}")

    choice = input("Do you want to validate and slice another email? y/n ")
    if choice not in ['y', 'Y', 'yes', 'YES']:
        break
