# Take int input from user
#  make copy of list

quantity = int(input("Quantity of inputs : "))
lst = []

for num in range(1,quantity+1):
    value = int(input("Enter {} value : ".format(num)))
    lst.append(value)

print(lst)
new_lst = lst.copy()
print(new_lst)

