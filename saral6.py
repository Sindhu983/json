import json

dic='{"a":1,"a":2,"a":3,"a":4,"b":1,"b":2}'
a=json.loads(dic)
b=json.dumps(a)
print(b)
