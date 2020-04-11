import re

name = input("Enter name of the file:")

if len(name) == 0 :
    name = "sample.txt"

try :
    handle = open(name)
except :
    print("Something wrong.")
    quit()

for line in handle :
    tmp = re.findall("^V.*:\s([0-9]+)", line)
    print(tmp)
