''' Simple Interest Calculator '''
try:
    while True :
        print("1. Simple Interest")
        print("2. Principal")
        print("3. Rate")
        print("4. Time (year)")
        print("5. Exist")
        choice_inp=input("Choose the a parameter you are looking for:")
        # for calculating the Interest
        if choice_inp == "1":
            P = float(input("Enter the Principal here :"))
            R = float(input("Enter the Rate here :"))
            T = float(input ("Enter the Time here :"))
            SI = (P*R*T)/100
            print(f"\n The Simple Interest is {SI}")
        # for calculating the Principal
        elif choice_inp == "2":
            R = float(input("Enter the Rate here :"))
            T = float(input ("Enter the Time here :"))
            SI = float(input("Enter the Interest here"))
            P = (SI*100)/(R*T)
            print(f"\n The Principal is {P}")
        # for calculating Rate
        elif choice_inp == "3":
            P = float(input("Enter the Principal here :"))
            T = float(input ("Enter the Time here :"))
            SI = float(input("Enter the Interest here"))
            R = (SI*100)/(P*T)
            print(f"\n The Rate is {R}")
        # for calculating Time
        elif choice_inp == "4":
             P = float(input("Enter the Principal here :"))
             R = float(input("Enter the Rate here :"))
             SI = float(input("Enter the Interest here"))
             T = (SI*100)/(PR)
             print(f"\n The Time is {T}")
        else:
             print("Have a nice day")
             break                  
except ValueError:
    print("Invalid Input")
