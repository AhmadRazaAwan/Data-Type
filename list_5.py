# check data available in list or not.
# or Check that its case sensitive.
# print list values one by one.

lst = ["Java", "Python", "C++", "Javascript"]

# it return True or False statement

# False
print("Swift" in lst)

# True
print("Java" in lst)

# its return False because its case sensitive
print("java" in lst)

# print one by one
for languages in lst:
    print(languages)