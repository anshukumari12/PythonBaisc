# # guest list
# setF = {"Alice","Bob","Charlie"}
# setS = {"Charlie", "David","Eve"}
# setN=setS.union(setF)
# print("union",setN)
# setN=setS.intersection(setF)
# print("INTERSECTION",setN)

# remove duplicates and add 6 number

# data=[1,2,2,3,4,4,4,4,5]
# data_set=set(data)
# data_set.add(6)
# print(data_set)

# libaray aduit

library_books = {"Hobbit", "1984", "Gatsby", "Odyssey", "Hamlet"}
checked_out = {"1984", "Hamlet"}
available_books = library_books - checked_out
print("Available books:", available_books)
new_book = "Don Quixote"
if new_book not in library_books:
    library_books.add(new_book)
print("Updated library books:", library_books)

# permission checker

user_permissions = {"read", "write"}
admin_reqs = {"read", "write", "execute"}
has_admin_access = user_permissions.issubset(admin_reqs)
print("Admin access:", has_admin_access)
missing_permissions = admin_reqs - user_permissions
print("Missing permissions:", missing_permissions)

# the log analyzer
 
logs = {
    "404": [10, 12, 15, 20],
    "500": [12, 20, 22, 25],
    "403": [10, 20, 30]
}

common_servers = {s for s in logs["404"] 
 if s in logs["500"] and s in logs["403"]}
print("Servers with all errors:", common_servers)
critical_servers = set(logs["500"]) - set(logs["404"])
print("Critical servers:", critical_servers)


