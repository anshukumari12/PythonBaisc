# Friends=["rohit","ram","aman","amit","dhruv"]
# new_friend=input("enter new friend:")
# Friends.append(new_friend)
# print(Friends)
# important_friend=input("enter import friend:")
# position=int(input("location for friend:"))
# Friends.insert(position,important_friend)
# print(Friends)


# # create list
# list2=[1,2,3,4,5,6,7,8,9,10]
# print(list)


# append,insert list

list1=[1,3,10,100,3,3,6,8] 
print(list1)
list1[3]=59
list1.append(5)
print(list1)
length=len(list1)
print("lenght of list:",length)

#  Find all of the words in a list of strings that are less than 4 letters

# words = ["hii","hello","how","are","you","aman"]
# result=[]
# for i in words:
#    if len(i)<4:
#       result.append(i)
#       print(result,end=",")

# Even / Odd list using range(20)

numbers = range(20)
result = []

for n in numbers:
    if n % 2 == 0:
        result.append("even")
    else:
        result.append("odd")

print(result)

# Numbers divisible by 7 (1–1000)

result = []

for i in range(1, 1001):
    if i % 7 == 0:
        result.append(i)

print(result)

# Count spaces in a string

text = input("Enter a string: ")
count = 0

for ch in text:
    if ch == " ":
        count += 1

print("Number of spaces:", count)

#Common numbers in two lists (NO set or tuple)

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common = []

for i in list_a:
    if i in list_b:
        common.append(i)

print(common)


