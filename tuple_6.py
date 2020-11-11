# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])

# Shows Error because tuples cannot be edit
# my_tuple[1] = 9

# However list elements can be change
# Tuple 3rd index because its list and list 0 index = 9
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('a', 'b', 'c', 'd', 'e')

# Output: ('a', 'b', 'c', 'd', 'e')
print(my_tuple)