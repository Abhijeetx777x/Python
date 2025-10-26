# CONDITIONAL STATEMENTS
# Q1

# age=int(input("Enter Your Age: "))

# if(age>=18):
#     print("Eligible to vote")
# else:
#     print("Not Eligible to vote")

# Q2

# light=input("Access Colour : ")
# if(light == "Green"):
#     print("Go")
# elif(light== "Yellow"):
#     print("Ready")
# elif(light == "Red"):
#     print("Stop")
# else:
#     print("Invalid")

# Q3

# Marks=int(input("Enter Your Marks : "))

# if(Marks >= 90):
#     print("Grade-A")
# elif(90 > Marks >= 80):
#     print("Grade-B")
# elif(80 > Marks >= 70):
#     print("Grade-C")
# elif(Marks < 70):
#     print("Grade-D")
# else:
#     print("Room For Improvement")

# NESTED STATEMENTS

# age=90

# if(age >= 18):
#     if(age >= 80):
#         print("NOT ALLOWED TO DRIVE")
#     else:
#         print("CanDrive")
# else:
#     print("Cannot Drive")

# Q.1

# n=int(input("Enter a NO. : "))
# if(n%2 == 0):
#     print("The No. is EVEN")
# else:
#     print("The No. Is ODD")

# Q.2

# a=int(input("Enter the A value : "))
# b=int(input("Enter the B value : "))
# c=int(input("Enter the C value : "))
# d=int(input("Enter the D value : "))

# if(a>=b and a>=c and a>=d):
#     print(" A is Greatest ")
# elif(b>=c and b>=d):
#     print(" B is Greatest ")
# elif(c>=d):
#     print("C is Greatest")
# else:
#     print("D is Greatest")

# Q.3

# x=int(input("Enter a Value of x :"))

# if(x % 7 == 0):
#     print("Number is Multiple of 7")
# else:
#     print("Number is Nott a Multiple of 7")


# Dictionary


# student ={
#     "name":"Rahul",
#     "Subjects":{
#         "phy":56,
#         "chem":44,
#         "math":27
#     }
# }

# print(student["Subjects"])

# keys

# print(len(student.keys()))

# values

# print(student.values())

# coversion to tuples

# print(student.items())

#Access Any Key

# print(student.get("name"))

# Update

# new_dict={"name" : "Abhijeet" , "age" : 18}
# student.update(new_dict)
# print(student)

# Creation

# Dicto={}             #Empty dictionary
# Dicto["name"]="Abhijeet Pandey"
# print(Dicto)

# SET


# collection ={1,2,3,4,"wo","wo"}
# collection1 = set()         #Empty Set - Syntax

# print(type(collection1))
# print(collection)
# print(len(collection))
# print(type(collection))

# Q.1

# marks={}

# i=int(input("Enter Your Physics Marks:"))
# marks.update({"PHY" : i})

# i=int(input("Enter Your Maths Marks:"))
# marks.update({"Maths" : i})

# i=int(input("Enter Your English Marks:"))
# marks.update({"English" : i})

# print(marks) 

# Q.2

# values={"9.0",9}
# values2={
#     ("float",9.0),
#     ("Integer",9)
#     }
# print(values2)
# print(values)

# Loops

# count=1
# while count <= 5:
    # print("Hello")
    # count += 1

# Print numbers from 1 to 5 :

# i=5
# while i >= 1:
#     print(i)
#     i-=1

# Q.1

# i=1
# while i<=100:
#     print(i)
#     i+=1

# Q.2

# i=100
# while i>=1:
#     print(i)
#     i-=1

# Q.3

# i=1
# n=int(input("enter the no. whose Multiple are wanted : "))
# while i<=10:
#     print("The Multiplication of " ,n, "is" , n * i) 
#     i+=1

# Q.4

# n=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx < len(n):
    # print(n[idx])
    # idx+=1

# Q.5

# n=(1,4,9,16,25,36,49,64,81,100)
# x=36

# i=0
# while i<len(n):
#     if(n[i]==x):
#         print("FOUND AT INDEX : ", i)
#     i+=1

# Break and Continue

# i=1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue      #Skip
#     print(i)
#     i+=1

# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break      #Ends Here
#     i+=1

#For Loop

# tup=(1,2,3,4,5)

# for num in tup:
#     print(num)
# else:
#     print("END")

# Q.1

# List=[1,4,9,16,25,36,49,64,81,100]

# for num in List:
#     print(num)
# else:
#     print("end")

# Q.2

# List = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# idx = 0
# for num in List:
#     if(num == x):
#         print("X is Founded at index",idx)
#         break
#     idx += 1
# else:
#     print("end")

# Def function

# 1.

# def Calc_sum(a,b):
#     return a+b

# sum = Calc_sum(1,2)
# print(sum)

# 2.

# def PrintHello():
#     print("HELLO")

# PrintHello()

# 3.

# def Average_no(a,b,c):
#     return (a+b+c)/3

# avg=Average_no(98,97,95)
# print(avg)

# Q.1

# City=["Delhi","Ghaziabad","Noida","Gurgaon","Chennai","Mumbai"]

# def print_len(list):
#     print(len(list))

# print_len(City)

# Q.2

# def printList(list):
    # for item in list:
        # print(item , end=" ")
# print()
# printList(City)

# Q.3


# def calc_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# calc_fact(5)

# Q.4

# def convertor(usd_value):
#     inr_value=usd_value*83
#     print(usd_value,"USD =",inr_value,"INR")

# convertor(2)

# q.5

# def Identify(number):
#     if(number%2==0):
#         print("EVEN")
#     else:
#         print("ODD")

# Identify(2) 
print("hello")