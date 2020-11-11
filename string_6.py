# String Methods

text = "I'm using Python 3"

# Original String Display
print("Original Text : ",text)

# All string convert into lower case
new_1 = text.lower()
print("String become lower : ",new_1)

# All string convert into Upper case
new_2 = text.upper()
print("String become upper : ",new_2)

# find u from the variable
new_3 = text.find("u")
print("It's Return the starting index of u :", new_3)

# Replace the old str to new
new_4 = text.replace("Python 3","Java")
print(new_4)

# It will split one string into list
new_5 = text.split()
print(new_5)

# It will join the list into one string
new_6 = ' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
print(new_6)
