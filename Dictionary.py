sentence = "python is easy and python is very easy"

words = sentence.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)

# # student grade marks

# marks = {
#     "Aman": 90,
#     "Riya": 85,
#     "Karan": 75,
#     "Neha": 90
# }

# total = sum(marks.values())
# average = total / len(marks)

# print("Average marks:", average)
# print("Students scoring above average:")

# for name, mark in marks.items():
#     if mark > average:
#         print(name)



# d1 = {'a': 50, 'b': 30, 'c': 70}
# d2 = {'b': 60, 'c': 65, 'd': 40}

# result = d1.copy()

# for key, value in d2.items():
#     if key in result:
#         result[key] = max(result[key], value)
#     else:
#         result[key] = value

# print(result)


# data = {
#     'name': 'Alice',
#     'city': 'Bangalore',
#     'course': 'Data Science'
# }

# max_key = ""
# max_len = 0

# for key, value in data.items():
#     if len(value) > max_len:
#         max_len = len(value)
#         max_key = key

# print(max_key)



# data = {
#     'a': 5,
#     'b': 15,
#     'c': 40,
#     'd': 60,
#     'e': 25
# }

# filtered = {}

# for key, value in data.items():
#     if 10 <= value <= 50:
#         filtered[key] = value

# print(filtered)


# votes = {}
# n = int(input("Enter number of voters: "))

# for i in range(n):
#     name = input("Vote for candidate: ")
#     votes[name] = votes.get(name, 0) + 1

# winner = max(votes, key=votes.get)

# print("Votes:", votes)
# print("Winner:", winner)




# data = {'a': 10, 'b': 20, 'c': 30}
# update = {'b': 200, 'c': 300}

# for key in data:
#     if key in update:
#         data[key] = update[key]

# print(data)






 
