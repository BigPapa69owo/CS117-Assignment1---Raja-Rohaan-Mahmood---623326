#Finds the longest continuous drop in battery voltage
v = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

cs = 0
bs = 0
bl = 1
cl = 1

for i in range(1, len(v)):
    if cl > bl:
        bl = cl
        bs = cs
    if v[i] < v[i - 1]:
        cl += 1
    else:
        cl = 1
        cs = i

if cl > bl:
    bl = cl
    bs = cs

e = bs + bl - 1

print("Longest continuous drop:", bl, "minutes")
print("Started at:", v[bs], "V")
print("Ended at:", v[e], "V")
