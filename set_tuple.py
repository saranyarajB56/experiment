
# set operations

a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b))
print(a.intersection(b))
print(a-b)
print(b-a)

# Dictionary operations
user = {"name":"saranya","age":"25","location":"kochi"}
print(user['name'],user["age"],user["location"])

num = [3,0,-1,6,-999,5,9,0,-10]
for i in num:
 if i > 0:
    print(i, "is positive number")
 elif i < 0:
  print(i, "is negative number")

