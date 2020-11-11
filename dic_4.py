# Use methods

info_dict = {1: 1, 2: 4, 3: 6, 4: 8, 5: 10}

# Before Pop
print(info_dict)

# name is remove from dictionary
info_dict.pop(2)
print(info_dict)

# Always remove from last
info_dict.popitem()
print(info_dict)

# Dictionary is clear no record they have
info_dict.clear()
print(info_dict)

# info_dic not exists
del info_dict
# Gives Error because no info_dict find
#print(info_dict)