import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL :")

if len(url) == 0 :
    url = "http://py4e-data.dr-chuck.net/comments_42.html"

try :
    html = urllib.request.urlopen(url, context = ctx).read()
except :
    print("Something wrong.")
    quit()

soup = BeautifulSoup(html, "html.parser")

tags = soup("span")

count = 0

for tag in tags :
    count = count + int(tag.contents[0])

print(count)
