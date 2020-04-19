import urllib.parse, urllib.request, urllib.error

urlservice = "http://maps.googleapis.com/maps/api/geocode/json?"
adress = input("Enter location")

url = urlservice + urllib.parse.urlencode({"adress":adress})

print(url)
