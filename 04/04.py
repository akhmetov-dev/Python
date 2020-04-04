def computepay( h, r ):
    if h < 40 :
        pay = h * r
    else :
        tmp = h - 40
        pay = 40 * r + tmp * 1.5 * r
    return pay

hours = input("Enter hours: ")
rate = input("Enter rate: ")

h = float(hours)
r = float(rate)

print ( "Pay", computepay( h, r ))