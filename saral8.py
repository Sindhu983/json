import json


# a=[["neelam","programer",24,2400],
# ["komal","trainer",24,20000],
# ["anuradha","HR",25,40000],
# ["Abhishek","manager",29,63000]]

# dic1={}
# i=0
# while i<len(a):
#     dic={}
#     j=0
#     while j<len(a[i])-3:
#         dic["name"]=a[i][j]
#         dic["Desigantion"]=a[i][j+1]
#         dic["age"]=a[i][j+2]
#         dic["salary"]=a[i][j+3]
#         j+=1
#     i+=1
#     dic1["emply1"]=dic
#     dic1["emply2"]=dic
#     dic1["emply3"]=dic
#     dic1["emply4"]=dic
#     print(dic1)
#     file=open("course.json","w")
#     json.dump(dic1,file,indent=4)



a=["neelam","programer",24,2400]
b=["komal","trainer",24,20000]
c=["anuradha","HR",25,40000]
d=["Abhishek","manager",29,63000]
e=["name","Designation","age","salary"]


dict={}
dic1={}
dic2={}
dic3={}
dic4={}
i=0
while i<len(a):
    j=0
    while j<len(a):
        dic1[e[i]]=a[i]
        dic2[e[i]]=b[i]
        dic3[e[i]]=c[i]
        dic4[e[i]]=d[i]
        j+=1
    dict["emply1"]=dic1
    dict["emply2"]=dic2
    dict["emply3"]=dic3
    dict["emply4"]=dic4
    i+=1
print(dict)
file=open("course.json","w")
json.dump(dict,file,indent=4)






