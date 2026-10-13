#Finds the highest, lowest and average of 7 voltage readings and counts those above 3.2 V
readings = (3.3,3.1,3.4,2.9,3.6,3.0,3.2)
max,min,sum,Vabove = 0,10000000000,0,0
for x in range(7):
    if readings[x] > max:
        max = readings[x]
    if readings[x] < min:
        min = readings[x]
    sum = sum + readings[x]
    if readings[x] > 3.2:
        Vabove = Vabove + 1
print("Readings above 3.2 V: ",Vabove)
print("Highest: ",max,"V")
print("Lowest: ",min,"V")
print("Average: ",sum/7,"V")

