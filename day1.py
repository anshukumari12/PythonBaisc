# student 5 marks total number and percentage
s=input("enter student name: ")
m=input("enter student class: ")
s=input("enter student section: ")
a=int(input("student marks in english: "))
b=int(input("student marks in c++:"))
c=int(input("student marks in python: "))
d=int(input("student marks in hindi: "))  
e=int(input("student marks java:  "))
m=a+b+c+d+e
print("total marks",m)
print("percentage",(m/500)*100)


#   3 number sum
a=int(input("enter 1 number: "))
b=int(input("enter 2 number: "))
c=int(input("enter 3 number: "))
d= a+b+c
print("sum of three number:",d)
 
#  3 number square
a=int(input("enter number:"))
print(a**2)
 
#   string format

a= input("enter a temperature: ")
celsuis= float(a)
fahrenheit = (celsuis * 9 / 5) + 32
print("Temperature in Celsius:", celsuis)
print("Temperature in Fahrenheit:", fahrenheit)


# Calculate quotient and remainder

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
quotient = num1 // num2
remainder = num1 % num2
print("Quotient:", quotient)
print("Remainder:", remainder)

# Calculate Simple Interest 

P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))
SI = (P * R * T) / 100
print("Simple Interest:", SI)

