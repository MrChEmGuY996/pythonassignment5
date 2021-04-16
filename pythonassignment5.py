
def options() :
    print("options")
    print("[P]: print options")
    print("[A]: Nmiles to Km")
    print("[B]: Km to Nmiles")
    print("[C]: C to F")
    print("[D]: F to C")
    print("[E]: Km to mi")
    print("[F]: mi to Km")
    print("[G]: cm to m")
    print("[H]: m to cm")
    print("[I]: yd to m")
    print("[J]: m to Yd")
    print("[K]: inches to cm")
    print("[L]: cm to inches")
    print("[Q]: quit")

options()

conversion = str(input("Type in a conversion from the list"))

while conversion != "Q" :

    if conversion == "P" :
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "A" :
        # 1 Nmile = 1.852km
        print("The conversion between Nautical miles and Kilometers is 1Nmile = 1.852Km")
        Nmiles = float(input("Enter the number for Nautical miles **Numerical values only**: "))
        Km = str(float(Nmiles * 1.852))
        print("Kilometers: ", Km)
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "B" :
        # 1 km = 0.539957 Nmiles
        print("The conversion between Kilometers and is Nautical miles is 1 km = 0.539957 Nmiles")
        Km = float(input("Enter the number for Kilometers **Numerical values only**: "))
        Nmiles = str(float(Km * 1.852))
        print("Nautical miles: ", Nmiles)
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "C":
        # ((C*(9/5)) + 32) = F
        print("The conversion between Celsius and Fahrenheit is ((C*(9/5)) + 32) = F")
        Celsius = float(input("Enter the number for Celsius **Numerical values only**: "))
        Fahrenheit = str(float(((Celsius * (9/5)) + 32)))
        print("Fahrenheit: ", Fahrenheit)
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "D":
        # ((F-32)*(5/9)) = C
        print("The conversion between Fahrenheit and Celsius is ((F-32)*(5/9)) = C")
        Fahrenheit = float(input("Enter the number for Fahrenheit **Numerical values only**: "))
        Celsius = str(float(((Fahrenheit -32)*(5/9))))
        print("Celsius: ", Celsius)
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "E":
        # 1Km = 0.621371mi
        print("The conversion between Kilometers and Miles is 1 km = 0.621371mi")
        Km = float(input("Enter the number for Kilometers **Numerical values only**: "))
        miles = str(float(Km * 0.621371))
        print("Miles: ", miles)
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "F":
        # 1mi = 1.60934Km
        print("The conversion between Miles and kilometers 1mi = 1.60934Km")
        miles = float(input("Enter the number for Miles **Numerical values only**: "))
        Km = float(miles * 0.621371)
        print("Kilometers: ", Km)
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "G":
        #1cm = 0.01m
        print("The conversion between Centimeters and meters is 1cm = 0.01m")
        cm = float(input("Enter the number for Centimeters **Numerical values only**: "))
        m = float(cm * 0.01)
        print("Meters: ", m)
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "H":
        #1m = 100cm
        print("The conversion between meters and Centimeters is 1cm = 0.01m")
        m = float(input("Enter the number for meters **Numerical values only**: "))
        cm = float(m * 100)
        print("Centimeters: ", cm)
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "I":
        # 1yd = 0.9144m
        print("The conversion between Yards and meters is 1yd = 0.9144m")
        Yd = float(input("Enter the number for Yards **Numerical values only**: "))
        m = float(Yd * 0.9144)
        print("Meters: ", m)
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "J":
        # 1m = 1.09361yd
        print("The conversion between meters and yards is 1m = 1.09361yd")
        m = float(input("Enter the number for meters **Numerical values only**: "))
        Yd = float(m * 1.09361)
        print("Yards: ", Yd)
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "K":
        # 1in = 2.54cm
        print("The conversion between inches and Centimeters is 1in = 2.54cm")
        inch = float(input("Enter the number for inches **Numerical values only**: "))
        cm = float(inch * 2.54)
        print("Centimeters: ", cm)
        options()
        conversion = str(input("Type in a conversion from the list"))

    elif conversion == "L":
        # 1cm = 0.393701in
        print("The conversion between Centimeters and inches is 1cm = 0.393701in")
        cm = float(input("Enter the number for Centimeters **Numerical values only**: "))
        inch = float(cm * 0.393701)
        print("Inches: ", inch)
        options()
        conversion = str(input("Type in a conversion from the list"))

    else :
        conversion = str(input("Type in a conversion from the list"))

print("The End")





