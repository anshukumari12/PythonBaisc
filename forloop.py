# sum  of natural number
a=int(input("enter first n number:"))
sum=0 
for i in range(a):
    sum+=i
print("sum of natural numaber",sum)

# multipication table
a=int(input("enter a number"))
for i  in range(1,11):

    print(a,"*",i,"=", a*i) 

# # palindrome
num = int(input("Enter a number: "))
rev = ""

for i in num:
    rev = i + rev 

if num == rev:
    print(num, "is a Palindrome")
else:
    print(num, "is NOT a Palindrome")



          
# print number 1to 100
n=int(input("enter a number "))
for i in range (1,101):  
   if n%3==0:
     print("fizz")
   elif n%5==0:
     print("buzz")
   elif n%3==0 and n%5==0 :
     print("fizzbuzz")

        
          


