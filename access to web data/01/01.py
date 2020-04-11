import re

name = input("Enter name of the file:")

if len(name) == 0 :
    name = "regex_sum_410867.txt"

try :
    handle = open(name)
except :
    print("Something wrong.")
    quit()

tmp = list()

sum = 0
count = 0

for line in handle :
    tmp = re.findall("([0-9]+)", line)
    for i in tmp :
        sum = sum + int(i)
        count = count + 1
        print(i)

print(count, sum)
