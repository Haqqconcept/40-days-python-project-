''' Multiplication table Generator '''

def multiply(num,limit):
    for i in range (1,limit+1):
        print(f" {i} x {num} = {i * num}")
while True:
    try:
         num = int(input("Enter the number you would wish to generate its table : "))
         limit = int(input("Enter the limit of the table : "))
         break
    except ValueError:
             print("Input a valide number please")
    
multiply(num,limit)

