

loop = True
while loop:
    
    pass_str = input("Please insert your password: ")
    loop = False #assume password is valid
    if len(pass_str) <8:
        loop = True
        print("Password length must be greater than 8")
    if not pass_str.isalnum():
        loop = True
        print("Password must not contain special characters")
    if pass_str.isdigit():
        loop = True
        print("Password must contain letters")
    if pass_str.isalpha():
        loop = True
        print("Password must contain digits")

print("okie")