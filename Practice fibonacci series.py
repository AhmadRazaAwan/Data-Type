a = [0,1]


def sum(n1, n2):
    return n1+n2


for i in range(0, 11):
    c = sum(a[-1], a[-2])
    a.append(c)

print(a)

# 0, 1, 1, 2, 3, 5, 8