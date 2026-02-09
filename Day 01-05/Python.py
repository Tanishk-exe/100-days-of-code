# dict={"name":'Tanishk',"age":20}
# print(dict)

# a=5
# b=10
# c=20
# d=17
# print("Addition is", a+b)
# print("Subtraction is", b-a)
# print("Multiply is", a*b)
# print("Division is", b/a)
# print(b**a)
# print(d%a)
# print(c//d)
# a ="Tanishk"
# print(a[-6:-3])


# # strings

# a="this is a test i am learning python for data science"
# print(a.upper())
# print(a.lower())
# print(a.rstrip("j"))
# print(a.replace("Tanishk", "ABc"))
# print(a.split())
# print(a.capitalize())
# print(a.startswith("t"))
# print(a.endswith("ce"))
# print(a.find("is"))


# a=int(input("Enter ur age: "))
# if(a>=18):
#     print("You can vote")
# else:
#     print("You cant vote")


# appleprice=100
# budget=int(input("Whats your budget::"))
# if(appleprice<=budget):
#     print("You can buy Apple",)
#     print("Remaining Balance:", budget- appleprice)
# else:
#     print("You cant buy apple")

# import time
# times=time.strftime("%H:%M:%S")
# print(times)

# name="Tanishk"
# for i in name:
#     print(i)

# list=["a","b","c","d"]
# for i in list:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(0,11,2):
#     print(i)

# for i in range(1, 1001):
#     print(i)

# i=0
# while(i<=10):
#     print(i)
#     i=i+1 

# def sum(a,b):
#     c=a+b
#     print(c)

# def isgreat(a,b):
#     if(a>b):
#         print("1st is great")
#     else:

#         print("Shut the f up")


# x=9
# y=5
# isgreat(x,y)

# list = [2,5,4,7,9]
# print(list)
# a=int(input("Enter no.:"))
# if a in list:
#     print("yes")
# else:
#     print("no")

# list=[5,8,2,5,0,9]
# list.append(90)
# list.reverse()
# m=[70,5,3,9]
# list.extend(m)
# list.insert(1, 7777)
# print(list)

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

# Plot
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()
    



