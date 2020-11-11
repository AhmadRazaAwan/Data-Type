# initialize my_set
my_set = {1, 3}
print(my_set)

# This command shows Error because they don't have sequence
# my_set[0]

# add value by using add method
my_set.add(2)
print("After Adding 2 in Sets", my_set)

# add multiple elements
my_set.update([2, 3, 4])
print(my_set)

# add list and set
my_set.update([4, 5], {1, 6, 8})
print(my_set)