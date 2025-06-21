''' Guessing Game  with pyhton '''
import random as rd
num = rd.randint(1,100)
user_name = input("Enter your name here : ")
def greet(user_name):
    print(f"Welcome {user_name.title()}, Are you ready for the game!")
greet(user_name)
attempt = 0
try:
 while True :
    guess = int(input(f"Dear {user_name.title()} , guess a number between 1 to 100 :"))
    attempt += 1
    if guess == num :
        print(f"Great! {num} is correct , your number of attempt(s) is {attempt}")
        break
    elif guess > num :
        print("Too high, try again ")
    else:
        print("Too low , try again")
except ValueError:
    print("Invalid Input")
