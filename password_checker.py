"""
Script gets a password from user then checks password strength (Strong, Medium, Weak).
Prints password, password strength, and suggestions for increasing password strength.
"""



def main():
    password = get_input()
    check_password(password)
    strong, errors = check_password(password)
    print_results(password, strong, errors)

def get_input():
    """ get user password, basic validation"""
    while True:
        password = input("Enter your password: ")
        if password == "":
            print("Please enter a password.")
        else:
            break
    return password

def check_password(password):
    """ measures password strength (length, case, numbers, special characters) """
    strong = True
    errors = []
    if len(password) < 8:
        strong = False
        errors.append("Password must be at least 8 characters.")
    if not any(char.isupper() for char in password):
        strong = False
        errors.append("Password must contain at least one uppercase character")
    if not any(char.islower() for char in password):
        strong = False
        errors.append("Password must contain at least one lowercase character.")
    if not any(char.isalnum() for char in password):
        strong = False
        errors.append("Password must contain one special character.")

    return strong, errors

def print_results(password, strong, errors):
    """ prints results with suggestions """
    if len(errors) >= 3:
        print(f"Password: {password} Strong? Weak")
    elif len(errors) > 1:
        print(f"Password: {password} Strong? Medium")
    else:
        print(f"Password: {password} Strong? Strong")
    for each in errors:
        print(each)


if __name__ == '__main__':
    main()