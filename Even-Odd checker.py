''' Even or odd Number Checker '''
try:
    while True:
            num = int (input("Enter a positive integer here (or 0 to exit)"))
            if num == 0:
                print("Bye! Have a nice day")
            elif num % 2 == 0:
                print (f"{num} is an Even Number")
                break
            elif num % 2 != 0 :
                print(f"{num} is an Odd Number")
except ValueError:
      print("Invalid input")
     
      
