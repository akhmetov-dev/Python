max = None
min = None

print("Enter a number")

while True :
    val = input(">")
    if val == "done" :
        break
    try :
        num = int(val)
    except :
        print("Invalid input")
        continue
    if max is None :
        max = num
    if min is None :
        min = num
    if max < num :
        max = num
    if min > num :
        min = num

print("Maximum is", max)
print("Minimum is", min)