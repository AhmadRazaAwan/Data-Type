
# Creating a Set
s = {"ahmad","raza","awan"}
print(s)

# Add aslam in Set
s.add("aslam")
print(s)

# Updating
s.update({"a","b","c"})
print(s)

# Check Length
print(len(s))

# Removing Elements
s.remove("aslam")
print(s)

# Make Set Frozen
new_s = frozenset(s)
print(new_s)
