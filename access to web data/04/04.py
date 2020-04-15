import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Input URL :")
if len(url) == 0 :
    url = "http://py4e-data.dr-chuck.net/comments_42.xml"

try :
    urlhandle = urllib.request.urlopen(url, context=ctx)
except :
    print("Something wrong.")
    quit()

data = urlhandle.read()
xmltree = ET.fromstring(data)

counts = xmltree.findall("comments/comment")
sum = 0

for val in counts :
    sum = sum + int(val.find("count").text)

print(sum)
