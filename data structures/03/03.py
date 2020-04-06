fname = input("Enter file name:")
try :
    fh = open(fname)
except :
    print("Incorrect input.")
    quit()

count = 0
sum = 0
for line in fh :
    if line.startswith("X-DSPAM-Confidence") :
        line = line.rstrip()
        line = line[19:]
        count = count + 1
        sum = sum + float(line)

average = sum / count
print("Average spam confidence:", average)