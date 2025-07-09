''' Simple Password Strenght Checker '''
import string
def password():
    while True:
        password = input("Enter your password")
        if len(password)< 8 :
            print("Try again, the password is less than 8 characters")
        elif not any(char.isupper() for char in password):
            print("Weak password: no Uppercase letter")
        elif not any (char.islower() for char in password):
            print("Weak password: no lowercase letter")
        elif not any (char.isdigit() for char in password):
            print("Weak password: Include at least a number ")
        elif not any (char in string.punctuation for char in password):
            print("Special Characters are missing")
        else:
            print ("Great password created successfully!")
password()
    
