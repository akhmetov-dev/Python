import json

data = dict()

data["name"] = "Nikita";
data["age"] = "22";
data["city"] = "Astrakhan";
data["zip"] = [1, 1, 7, 3, 9, 3];

data_json = json.dumps(data)

print(data_json)
