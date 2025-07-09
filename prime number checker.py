''' Prime Number checker '''
def checker():
    while True:
        try:
            num = int(input("Prime Number from :"))
            lim = int(input("To what number:"))
        except ValueError:
            print("Invalid Input, Enter an Integer please")
        for num1 in range (num,lim+1):
            for a in range (2, int(num1/2)+1):
                    if num1 % a == 0:
                     break
            else :
                print(num1 , end="-")
        break
checker()
                             
                         
                     

        
