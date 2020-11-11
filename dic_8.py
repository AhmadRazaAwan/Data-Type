# Find square using dictionary comprehension


square = {x: x * x for x in range(1, 11)}
print(square)

even_numbers = {x: x * x for x in range(11) if x % 2 == 0}
print(even_numbers)

odd_numbers = {x: x * x for x in range(11) if x % 2 == 1}
print(odd_numbers)