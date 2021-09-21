# hrs = work hours per week
hrs = input("Enter Hours:")
h = float(hrs)
# rph = rate per hour
rph = input("Enter Pay:")
r = float(rph)
if h <= 40 :
    print(h * r)
else :
    print((40 * r) + ((h - 40) * (1.5 * r)))
