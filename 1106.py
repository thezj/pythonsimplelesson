import json

data = {'a': 1, 'b': 2, 'xx': 4}

json_str = json.dumps(data)

with open('./testjson.json', 'w+') as f:
    f.write(json_str)

with open('./testjson.json', 'r') as f:
    rawjson = f.read()
    jsondata = json.loads(rawjson)
    print(jsondata['a'])

with open('./testjsontransform.json', 'w') as f:
    json.dump(data, f)
with open('./testjsontransform.json', 'r') as f:
    print(json.load(f)['xx'])
