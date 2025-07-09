''' Basic Login System '''
import getpass as getpass
username = "Abdulhaqq Abdulhakeem"
password = "Haqqconcept@123"
attempts = 0
while attempts < 3 :
    userinput = input( "Enter Your User_Name here:").strip()
    passwordinput = getpass.getpass( "Enter your password here :")   
    if (userinput == username) and (passwordinput == password) :
        print(f"{username}! Login Successfully")
        break
    else:
        attempts += 1
        print(f"{attempts} attempt(s)! ,Try again")
if attempts == 3 :
     print("Too many attempts. Access denied ")
    
