''' Random Password Generator '''
import random
lower_case = ["a","b","c","d",
              "e","f","g","h",
              "i","j","l","m",
              "n","o","p","u",
              "v","w","x","y",
              "z"
              ]
Upper_case = ["A","B","C","D",
              "E","F","G","H",
              "I","J","K","L",
              "M","N","O","P",
              "Q","R","S","U",
              "V","W","X","Y",
              "Z"
              ]
numbers = ["1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","&","*","|"]

password_pool = lower_case + Upper_case + numbers + symbols
while True:
    try:
        print("\n Random Password Generator")
        print("\n Choose from the following options")
        print("1. Letters Only")
        print("2. Letters and numbers")
        print("3. Letters,numbers, and symbols")
        user = input("How do you wants your password to like? select (1-3)")
        limit = int(input("How long do you want the password to be ?"))
        password = "" 
        if user == "1":
                for x in range (limit):
                    password += random.choice(lower_case + Upper_case)
        elif user == "2":
                for x in range (0,limit+1):
                    password += random.choice(lower_case + Upper_case + numbers)
        elif user == "3":
            for x in range (0,limit+1):
                password += random.choice(password_pool)
        else:
            print("Invalid selection. Choose 1,2 or 3")
            continue
        print(f"Generated password :{password}")
        again = input("Do you want to generate another password ? (yes or no)")
        if again.lower() != "yes":
            break
    except ValueError:
        print("Invalid Input, Please try again") 
                
    

