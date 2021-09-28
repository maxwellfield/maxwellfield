def computepay(hours, rate) :
    # print("In computepay", hours, rate) --> Module didn't want this for match
    if hours > 40 :
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else :
        pay = hours * rate
    # print("Returning",pay) -->Module didn't want this for match
    return pay

# hrs = work hours per week
# rph = rate per hour
hrs = input("Enter Hours:")
rph = input("Enter Pay:")
h = float(hrs)
r = float(rph)

xp = computepay(h,r)

print("Pay",xp)
# removed semi-colon after Pay because Module didn't want this for match
