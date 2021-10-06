l=[1,2,3,4,5]
l1=[5,6,7,8,9]
# Union=[]
# for i in l:
#     Union.append(i)
#     for j in l1:
#         Union.append(j)
# print(list(set(Union)))



# #########################intescetion for loppp 

# intersction=[]
# for i in range(len(l)):
#     for j in range(len(l1)):
#         if l[i]==l1[j]:
#             intersction.append(l[i])
# print(intersction)

# ##########################******whileloop
inters=[]
i=0
while i<len(l):
    j=0
    while j<len(l1):
        if l[i]==l1[j]:
            inters.append(l[i])
        j=j+1
    i=i+1
print(inters)

