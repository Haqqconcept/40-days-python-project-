''' Age checker and vote eligibility'''
import datetime as dt
user_name=input("Enter your full name here :")
dob_input = input("Enter your Date of Birth (YYYY-MM-DD): ")
try:
    # converting input string to date object
    dob = dt.datetime.strptime(dob_input, "%Y-%m-%d")
    today = dt.datetime.today()
    age = today.year - dob.year - ((today.month, today.day)< (dob.month, dob.day))
    print(f"\n Welcome {user_name.upper()}, you are {age} years old currently.")
    # checking if the user is eligible to vote in Nigeria
    if age >= 18:
        print (f"Congratulation, Dear {user_name} you are eligible to vote.\n Your Voter's Card will be issued very soon")
    else:
        rcm_year = 18 - age
        print(f"Sorry, Dear {user_name} you will need to come back in {rcm_year} years time. ")
except ValueError:
    print("Invalid date format! Please enter the date in  YYYY-MM-DD format.")
