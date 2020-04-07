fname = input("Enter file name: ")

try :
    fh = open(fname)
except :
    print("Incorrect output.")
    quit()

lst = list()
tmp = list()

for line in fh:
    line = line.rstrip()
    tmp = line.split()
    for word in tmp :
        if word not in lst :
            lst.append(word)

lst.sort()
print(lst)