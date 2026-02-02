# # args
# def average_marks(*args):
#     valid_marks = []

#     for mark in args:
#         if mark >= 0:
#             valid_marks.append(mark)

#     if len(valid_marks) == 0:
#         return 0

#     return sum(valid_marks) / len(valid_marks)

# kawgrs
def filter_details(**kwargs):
    for key, value in kwargs.items():
        if isinstance(value, str):
            print(f"{key} = {value}")
filter_details(name="Anshu", age=20, city="Delhi", marks=85)
