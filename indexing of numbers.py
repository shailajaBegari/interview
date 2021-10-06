# n=[3,4,5,6]
# # m=n.index(5)
# # print(m)

# n1=int(input("enter the number:"))
# i=0
# while i<len(n):
#     if n1==n[i]:
#         print(i)
#         break
#     i=i+1
    

# n=["s_shailu","lu_kky"]
# i=0
# s=[]
# while i<len(n):
#     j=0
#     string=""
#     while j<len(n[i]):
#         if n[i][j]=="_":
#             pass
#         else:
#             string+=n[i][j]
#         j=j+1
#     i=i+1
#     s.append(string)
# print(s)







# a=[10,20]
# b=[10,20]
# c=a
# print(a==b)






# print( (3**2)//2 )



# def func(x):

#   res = 0

#   for i in range(x):

#      res += i

#   return res



# print(func(4))
# def power(x, y):

#   if y == 0:

#     return 1

#   else:

#     return x * power(x, y-1)

		

# print(power(2, 3))


# try:

  
#     with  open("test.txt") as f:

#         print(f.read())


# except:
#     print("Error")



# nums = [1, 2, 8, 3, 7]

# res = list(filter(lambda x: x%2==0, nums))

# print(res)


# nums = (55, 44, 33, 22)

# print(max(min(nums[:2]), abs(-42)))


# try:

#   print(1)

#   print(20 / 0)

#   print(2)

# except ZeroDivisionError:

#   print(3)

# finally:

#   print(4)



# a = (lambda x: x*(x+1)) (6)
# print(a)

file = open("/usercode/files/books.txt", "r")

fileLines = []
for lines in file:
	fileLines.append(lines)
length = 1
for n in fileLines:
	if length == len(fileLines):
		print(n[0] + str(len(n)))
	else:
		print(n[0] + str(len(n)-1))
	length += 1
file.close()
