user=int(input("enter the solders wepans:"))
i=0
list1=[]
while i<user:
    wepans=int(input("person holding  wepans:"))
    list1.append(wepans)
    i=i+1
print(list1)
i=0
e_count=0
o_count1=0
while i<len(list1):
    if list1[i]%2==0:
        e_count=e_count+1
    else:
        o_count1=o_count1+1
    i=i+1
print("evencount",e_count)
print("oddcount",o_count1)
if e_count>o_count1:
    print(" READY FOR BATTEL")
# elif e_count==o_count1:
#     print("NOT READY")
else:
    print("NOT READY ")