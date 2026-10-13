#Calculates the total resistance of resistors connected in series
howmanyresistors = int(input("How many resistors? "))
rtotal = 0
for x in range(1,howmanyresistors + 1):
    cont = int(input(f"Enter R{x}: "))
    rtotal = cont + rtotal
print("Total resistance =", rtotal,"ohm")
