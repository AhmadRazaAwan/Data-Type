# how to change items in Tuples
# fist convert tuple into list because tuples are not edit able.
# replace value with index
# list are edit able.
# After that again change list into tuple

tpl = ("Java", "Python", "C++", "Javascript")
print("Before changing value :", tpl)

lst1 = list(tpl)
lst1[3] = "Html"
tpl = tuple(lst1)
print("After changing value :", tpl)

lst1 = list(tpl)
lst1[1:3] = ["Css", "Swift"]
tpl = tuple(lst1)
print("After changing value :", tpl)