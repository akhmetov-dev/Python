import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
if len(url) == 0 :
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

count = int(input("Enter count of transitions:"))
position = int(input("Enter position to transitions:"))

try :
    html = urllib.request.urlopen(url, context = ctx).read()
except :
    print("Incorrect url.")
    quit()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

while count > 0 :
    print(tags[position - 1].contents[0])
    url = tags[position - 1].get('href', None)
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = count - 1
