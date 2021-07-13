import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
} 

#out_file = open("myfile.json", "w")

with open("my_file.json","w") as json.file:
    json.dump(dict1,json.file,indent=4)



# import json

# a={'navgurukul': 3}
# mystring = json.dumps(a)
# print(mystring)
# print(type(mystring))
 
