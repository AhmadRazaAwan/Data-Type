# Take union, intersection, difference, symmetric_difference using set
# because these method are made for sets

my_set1 = {'a','b','c'}
my_set2 = {'c','d','e'}

result = my_set1.union(my_set2)
# result = my_set1 | my_set2
print(result)

result1 = my_set1.intersection(my_set2)
# result1 = my_set1 & my_set2
print(result1)

result2 = my_set1.difference(my_set2)
# result2 = my_set1 - my_set2
print(result2)

result3 = my_set1.symmetric_difference(my_set2)
# result3 = my_set1 ^ my_set2
print(result3)