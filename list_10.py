# Take 5 integer inputs from user and store them in a list.
# Again ask user to give a number. Now, tell user whether that number is present in list or not.

lst = []

for i in range(1,6):
    value = int(input("Enter {} number : ".format(i)))
    lst.append(value)

search = int(input("Enter number to check present or not : "))

if search in lst:
    print("Present")
else:
    print("Not Present")