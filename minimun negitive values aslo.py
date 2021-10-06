x=[1,2,0,3,4,8,9,54,-1]
i=0
min=0
while x[i:]:
    if x[i]<min:
        min=x[i]
        x[i]=min
    i+=1
print(min)
        