# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 00:11:26 2025

@author: USER
"""

# student grade management system
students={}
def add_students():
    while True:
       name=input("Enter the  name of students here (or type 'exit' to stop):").strip()
       if name.lower() == "exit":
           break
       if name in students :
            print(f"{name} already exists in the records")
            overwrite = input("do you want to overwrite the existing grades ? (yes/no) :").strip().lower()
            if overwrite != "yes":
               print("Skipping student.")
               continue 
               
       grades_input = input(f"Enter the grades for {name}, separated by a comma (e.g 3,4,5,6,7)").strip()
       try:
          grades = list(map(int, grades_input.split(',')))
       except ValueError:
             print("Invalid input , Please enter numeric grades separated by comma ")
             continue
       students[name] = grades 
       print(f"Student {name} with grades {grades} has been added successfully!\n")
def display_students():
    if not students :
        print("No students records available")
    else:
        print("\n student records :")
        for name,grades in students.items():
            print(f"{name}:{grades}")
    print()

while True :
    print("\n Choose an option")
    print("1. Add Students")
    print("2. View all Students")
    print("3. Exit")
    choice = input("Enter your Choice (1/2/3):").strip()
    if choice == "1":
       add_students()
    elif choice == "2":
        display_students()
    elif choice == "3":
       print("Exiting the program. Goodbye!")
       break
    else:
        print("Invalid choice. Please enter 1, 2, or 3")
    
