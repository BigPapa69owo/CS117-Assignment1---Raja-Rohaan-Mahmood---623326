#Converts a decimal number into binary
def decimal_to_binary(x):
    if x == 0:
        return 0
    sx = ""
    rx = x
    cx = x
    while rx > 1:
        rx = rx // 2
        sx = str(cx % 2) + sx
        cx = rx
    return "1" + sx

print(decimal_to_binary(10))
print(decimal_to_binary(25))
