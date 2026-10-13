#Converts a resistor colour band into its digit
band = str(input("Enter band colour: "))
if band.lower() == "black":
    print("Digit =", 0)
elif band.lower() == "brown":
    print("Digit =", 1)
elif band.lower() == "red":
    print("Digit =", 2)
elif band.lower() == "orange":
    print("Digit =", 3)
elif band.lower() == "yellow":
    print("Digit =", 4)
elif band.lower() == "green":
    print("Digit =", 5)
elif band.lower() == "blue":
    print("Digit =", 6)
elif band.lower() == "violet":
    print("Digit =", 7)
elif band.lower() == "grey":
    print("Digit =", 8)
elif band.lower() == "white":
    print("Digit =", 9)
else:
    print("Invalid colour")
