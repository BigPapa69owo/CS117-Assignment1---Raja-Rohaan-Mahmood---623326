#Shows the direction of current flow between A and B
I = int(input("Enter value of current: "))
if I > 0:
    print("Current flows from A to B")
elif I < 0:
    print("Current flows from B to A")
else:
    print("No current flows")
