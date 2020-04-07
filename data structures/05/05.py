fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try :
    fh = open(fname)
except :
    print("Incorrect input")
    quit()

count = 0
tmp = list()
mails = list()

for line in fh :
    if "From " in line :
        tmp = line.split()
        mails.append(tmp[1])
        count = count + 1
        print(tmp[1])

print("There were", count, "lines in the file with From as the first word")