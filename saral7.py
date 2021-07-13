import json

dic={}
file=open("Text.txt","r")
for line in file:
    key,value=line.strip().split(None,1) #reads each line and trims of extra the spaces 
    dic[key]=value.strip()               #and gives only the valid words
print(dic)
