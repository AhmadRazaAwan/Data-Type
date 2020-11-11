
marks = {}.fromkeys(["English", "Maths", "Programming"])
print(marks)

marks = {}.fromkeys(["English", "Maths", "Programming"],0)
print(marks)

marks = {}.fromkeys(["Maths", "English", "Programming"],3)
print(marks)

print(list(sorted(marks.keys())))