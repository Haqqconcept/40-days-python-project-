# DAY 3
# TEMPERATURE CONVERTER
value1 = float(input("Enter the temperature value here :"))

while True :
    print(f"Choose one of the following Units:")
    print("1. Fahrenheit")
    print("2. Celsius")
    print("3. Kelvin")
    print("4. Rankine")
    unit=input("Select 1,2,3or 4 :")
    if unit == "1":
        Fahreheit = value1
        Celsius = Fahrenheit - 32
        kelvin = Celsius + 273.15
        Rankine = Fahrenheit + 459.67
        print(f"1.The value in Celsius : {Celsius},\n 2. The value in Kelvin : {kelvin},\n 3. The value in Rankine : {Rankine} ")
    elif unit=="2":
        Celsius = value1
        frh = 1.8 * Celsius + 32
        klv = Celsius + 273.15
        Rk = 1.8 * Celsius + 491.67
        print(f"1.The value in Fahreheit : {frh},\n 2. The value in Kelvin : {klv},\n 3. The value in Rankine : {Rk} ")
    elif unit == "3" :
        kelvin = value1
        frh = 1.8(kelvin - 273.15)+32
        cls = kelvin - 273.15
        Rk = 1.8 * kelvin
        print(f"1.The value in Celsius : {cls},\n 2. The value in Fahrenheit : {frh},\n 3. The value in Rankine : {Rk} ")

    elif unit == "4":
        Rankine = value1
        frh = Rankine - 459.67
        cls = (5/9)(Rankine - 491.67)
        klv = Rankine * 5/9
        print(f"1.The value in Celsius : {cls},\n 2. The value in Kelvin : {klv},\n 3. The value in Fahrenheit : {frh} ")
    
    else:
       print("Select one of the options")
    break
print(" Have a nice day ")
