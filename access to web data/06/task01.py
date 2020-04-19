import urllib.parse, urllib.request, urllib.error
import json

url = input("Enter URL to parse:")

if len(url) == 0 :
    url = "http://py4e-data.dr-chuck.net/comments_42.json"

try :
    url_handler = urllib.request.urlopen(url)
except :
    print("Something wrong.")
    quit()

url_content = url_handler.read().decode()

json_dict = json.loads(url_content)

sum = 0

for item in json_dict["comments"] :
    sum = sum + item["count"]

print(sum)
