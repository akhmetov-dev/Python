name = input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"

try :
    handle = open(name)
except :
    print("Something wrong.")
    quit()

hist = dict()
tmp = list()

for line in handle :
    if "From " in line :
        line.rstrip()
        tmp = line.split()
        hist[tmp[1]] = hist.get(tmp[1], 0) + 1

val = None

for k, v in hist.items() :
    if val == None :
        val = v
    if val < v :
        val = v
        key = k

print(key, val)
