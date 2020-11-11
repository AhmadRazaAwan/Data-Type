# Concatenation
# We can combine tuples
# Tuple can be multiply

# Output: (1, 2, 3, 4, 5, 6)
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)

result1 = tpl1 + tpl2
print("Two Tuples can be add", result1)

result2 = tpl1 + tpl1
print("one tuple can be add", result2)

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)
print((tpl1) * 2)