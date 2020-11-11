# we can insert value in list


lst = ["a", "b", "c", "d"]
print("Orignal List : ", lst)

# if we want to insert value on specific index then we use insert.
print("Insert z in 0 index")
lst.insert(0,"z")
print(lst)

# append always add value in last
print("Append i")
lst.append("i")
print(lst)

# Extending lists in Python
print("Extend list with ['a', 'b', 'c']")
lst.extend(["a", "b", "c"])
print(lst)

# remove method use to remove value
print("Remove i")
lst.remove('i')
print(lst)

# del use to delete
# delete 1 index value
del lst[1]
print(lst)

# del use to delete
# delete the complete list

# del lst
# print(lst)

