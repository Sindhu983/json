import json

dic={
    "name":"navgurukul",
    "year":2017,
    "pet":"slessy",
    "students": [
            {"dhanu":"maharasta"},
            {"priya":"vizag"}
            ]
    }

a=json.dumps(dic,indent=1)
print(type(a))
print(a)

