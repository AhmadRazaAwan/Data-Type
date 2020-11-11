# use remove, pop with index, pop without index, clear list.

my_list = ['a','b','c','d','e','f','g']
print(my_list)

my_list.remove('f')
# Output: ['a', 'b', 'c', 'd', 'e', 'g']
print(my_list)

# Output: 'b'
print(my_list.pop(1))

# Output: ['a', 'c', 'd', 'e', 'g']
print(my_list)

# Output: 'g'
print(my_list.pop())

# Output: ['a', 'c', 'd', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)