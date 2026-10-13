#Checks if fuse blows or not
voltage = int(input("Enter voltage (V): "))
resistance = int(input("Enter resistance (ohm): "))
if resistance > 0:
    current = voltage/resistance
    print(f"Current = {current} A")
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
else:
    print("Invalid Resistance")
