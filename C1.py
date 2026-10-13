#Calculates current and power dissipated using functions
def ohms_current(v,r):
    current = v / r
    return current

def power_dissipated(i,r):
    power = (i*i) * r
    return power

V = int(input("Enter a value of voltage: "))
R = int(input("Enter a value of resistance: "))
if R > 0:
    I = ohms_current(V,R)
    P = power_dissipated(I,R)
    print(f"Current = {I} A")
    print(f"Power = {P} W")
else:
    print("Enter a valid resistance value")
