num1=float(input("Enter your first number here : "))
num2=float(input("Enter your second number here :"))
while True :
    print("\n Choose an operation !")
    print("1. Addition (+)")
    print("2. Substraction (-)")
    print("3. Multiplication(*)")
    print("4. Division (/)")
    print("5. Exist")
    choice = input("Enter your choice here:").strip()
    if choice == "1":
        result = num1+num2
    elif choice == "2":
        result = num1-num2
    elif choice == "3":
        result = num1*num2
    elif choice == "4":
        if num2 != 0 :
           result = num1/num2
        else:
            print("Invalid Syntex")
    elif choice == "5":
        print("Goodbye , glad you enjoyed the program")

        result = None
    if result is not None:
        print(result)
        break
    else:
        print("Invalid choice. Please enter 1, 2 , 3, 4,or 5.")
while True :
    num2 = float(input("Enter your number here :"))
    print("\n Choose an operation !")
    print("1. Addition (+)")
    print("2. Substraction (-)")
    print("3. Multiplication(*)")
    print("4. Division (/)")
    choice = input("Enter your choice here:").strip()
    if choice == "1":
        result = float (result )+ num2
    elif choice == "2":
        result = float(result)-num2
    elif choice == "3":
        result = float(result)*num2
    elif choice == "4":
        if num2 != 0 :
           result = float(result)/num2
        else:
            print("Invalid Syntex")
            continue
        print(f"Updated result: {result}")
        
        break
    print(result)

    
        
