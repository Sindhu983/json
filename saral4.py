import json

dic={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
#dic1={}
a=json.dumps(dic,sort_keys=True)
print(a)


