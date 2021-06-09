while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print("Select a new password (letter and numbers only) and must of 6+ chars:")
    password = input()
    if len(password) > 6:
        if password.isalnum():
            break
        else:
            print("Password can only have letters and numbers.")
    else:
        print("Password must be of more than 6 characters")
