# Accessing Dictionary Objects

my_dict = {"name": 'Raza', "age":  23}
print(my_dict)
print(my_dict["name"])
print(my_dict["age"])

# It's shows Error
# print(my_dict["course"])

# It's not showing Error Return None statement
print(my_dict.get("course"))

# in this command course key have values so they print
print(my_dict.get("course",["python", "Swift"]))