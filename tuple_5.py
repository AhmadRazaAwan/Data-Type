# check data available in tuple or not.
# or Check that its case sensitive.
# print tuples values one by one.

tpl = ("Java", "Python", "C++", "Javascript")

# it return True or False statement

# False
print("Swift" in tpl)

# True
print("Java" in tpl)

# its return False because its case sensitive
print("java" in tpl)

# print one by one
for languages in tpl:
    print(languages)