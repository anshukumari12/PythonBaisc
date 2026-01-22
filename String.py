# # string length,add
# str=(input("enter a  number:"))
# if len(str) <2:
#     print(" not valid")
# else: 
#     result=(str[:2]+str[-2:])
#     print(result)   

# # swap string
# str1="coder"
# str2="roots"
# new1=str2[0]+str1[1:]
# new2=str1[0]+str2[1:]

# print(new1,new2)

# swap,string length
# str=(input("enter a string:"))
# if len(str)>3:
#     print(str+"ly")
# else:
#     print(str+"ing")    

# Write a Python program to remove the nth index character from a nonempty string
 
str=(input("enter a string"))
n=int(input("enter a number to delete a string"))
new_string=str[:n]+str[n+1:]
print(new_string)







