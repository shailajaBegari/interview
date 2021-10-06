custmars=int(input("how many members ordering custmers:"))
person=1
list1=[]
dic={}
while person<=custmars:
    order=int(input("ordering time:"))
    prepation=int(input("eneter the prepatarion time:"))
    delivary=order+prepation
    dic[person]=delivary
    list1.append(delivary)
    person=person+1
print(dic)
list1.sort()
print("sorted  Time:",list1)
list2=[]
for i in list1:
    for key in dic:
        if i==dic[key]:
            list2.append(key)
print("sorted persons:",list2)
i=0
list3=[]
while i<len(list2):
    if list2[i] not in list3:
        list3.append(list2[i])
    i=i+1
print(list3)








