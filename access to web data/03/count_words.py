import urllib.request, urllib.parse, urllib.error

url_name = input("Enter URL:")

if len(url_name) == 0 :
    url_name = "http://data.pr4e.org/romeo.txt"

try :
    fhand = urllib.request.urlopen(url_name)
except :
    print("Something wrong.")
    quit()

counts = dict()

for line in fhand :
    words = line.decode().split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

listvk = list()

for k, v in counts.items() :
    newtup = (v, k)
    listvk.append(newtup)

listvk = sorted(listvk)

for v, k in listvk :
    print(k, v)
