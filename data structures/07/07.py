name = input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"

try :
    handle = open(name)
except :
    print("Something wrong")
    quit()

counts = dict()

for line in handle :
    if "From " in line :
        line.rstrip()
        tmp1 = line.split()
        tmp2 = tmp1[5].split(":")
        counts[tmp2[0]] = counts.get(tmp2[0], 0) + 1

for k, v in sorted(counts.items()) :
    print(k, v)
