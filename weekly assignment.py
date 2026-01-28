# print number 1to 50
n=int(input("enter a number "))
for i in range (1,51):  
   if n%3==0:
     print("fizz")
   elif n%5==0:
     print("buzz")
   elif n%3==0 and n%5==0 :
     print("fizzbuzz")

    #  prime number  
   for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")


 # grade sum
    score = int(input("Enter score: "))

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score <= 89:
    print("Grade B")
elif 70 <= score <= 79:
    print("Grade C")
elif 60 <= score <= 69:
    print("Grade D")
else:
    print("Grade F")


    # table print
    n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#   1 to 20 square 
squares = []
for i in range(2, 21, 2):
    squares.append(i * i)

print(squares)

# leap year check
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# type of triangle
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
elif a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
    print("Right Angle Triangle")
else:
    print("Scalene Triangle")

    # positive,negative,zero
    num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# bmi calaculator
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)
print("BMI:", bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")

    # days of week
    day = int(input("Enter day number (1-7): "))
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
if 1 <= day <= 7:
    print(days[day-1])
else:
    print("Invalid day")

    # discount calaclation
    price = float(input("Enter price: "))
if price > 1000:
    discount = price * 0.10
elif price >= 500:
    discount = price * 0.05
else:
    discount = 0
print("Discount:", discount)
print("Final Price:", price - discount)

# sum of n natural no
n = int(input("Enter n: "))
sum = n * (n + 1) // 2
print("Sum:", sum)

# salary employee
employee_details = {
    1: {"name": "A", "dept": "IT", "salary": 60000},
    2: {"name": "B", "dept": "HR", "salary": 45000},
    3: {"name": "C", "dept": "Finance", "salary": 70000}
}
result = []
for emp in employee_details.values():
    if emp["salary"] > 50000:
        result.append(emp["name"])
print(result)

# count vowel
s = input("Enter string: ")
count = 0
for ch in s.lower():
    if ch in "aeiou":
        count += 1
print("Vowels:", count)

# sum of digit
num = input("Enter number: ")
sum = 0
for d in num:
    sum += int(d)
print("Sum of digits:", sum)

# star pattern
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print("*" * i)

    # even no n number
    n = int(input("Enter number: "))
for i in range(2, n + 1, 2):
    print(i, end=" ")

    # list operation

    lst = [10, 25, 30, 25, 40, 50, 60, 25, 70, 80]

print("25 exists:", 25 in lst)
print("Length:", len(lst))
print("Occurrence of 25:", lst.count(25))

print("Traverse:")
for i in lst:
    print(i)

print("Even numbers:")
for i in lst:
    if i % 2 == 0:
        print(i)

# string operation

s = input("Enter string: ")
words = s.split()

print("Length:", len(s))

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

print("Middle word:", words[len(words)//2])
print("Second last word:", words[-2])

# calculator menu

print("1. Power\n2. Sum\n3. Sub\n4. Multiply")
ch = int(input("Enter choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if ch == 1:
    print(a ** b)
elif ch == 2:
    print(a + b)
elif ch == 3:
    print(a - b)
elif ch == 4:
    print(a * b)
else:
    print("Invalid choice")

# count matching strings
X = ['abc', 'xyz', 'aba', '1221']
count = 0

for s in X:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print(count)












