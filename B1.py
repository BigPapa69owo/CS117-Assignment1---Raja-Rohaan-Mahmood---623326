#Prints voltage and current values for a 10 ohm resistor from 1 V to 10 V
R = 10
for x in range(10):
    print("V =", x+1,"V, I =", (x+1)/R,"A")
