import json

data = '''
{
    "name" : "Nikita",
    "phone" : {
        "type" : "intl",
        "number" : "+7 977 446 72 xx"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)

print("Name:", info["name"])
print("Hide:", info["email"]["hide"])
