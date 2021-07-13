import json

dic={}
dict={}
user=int(input("enter the number :"))
i=0
while i<user:
    user=input("enter the input :")
    user2=int(input("enter the number :"))
    dic[user]=user2
    i+=1
    dict["shopping_list"]=dic
file=open("shopping_list","w")
json.dump(dict,file,indent=4)


    
