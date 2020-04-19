import json

x = '''
{
    "name":"Nikita",
    "age":22,
    "city":"Astrakhan",
    "zip":[1,1,7,3,9,3]
}'''

y = json.loads(x)

print(y["name"])
print(type(y["name"]))

print(y["age"])
print(type(y["age"]))

print(y["city"])
print(type(y["city"]))

print(y["zip"])
print(type(y["zip"]))
