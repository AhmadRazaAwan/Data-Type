# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard 4
my_set.discard(4)
print(my_set)

# remove 6
my_set.remove(6)
print(my_set)

# discard 4
# not present in my_set
# Program continue
my_set.discard(2)
print(my_set)

# remove 2
# not present in my_set
# give error
my_set.remove(2)