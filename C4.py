#Calculates the output voltage of a voltage divider with and without a load resistor
def loaded_divider(vs, r1, r2, rl):
    voltageu = vs*r2/(r1+r2)
    rtotal = r2*rl/(r2+rl)
    vloaded = vs*rtotal/(r1+rtotal)
    return voltageu, vloaded

print(loaded_divider(12, 1000, 1000, 500))
