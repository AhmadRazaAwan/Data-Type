# Python offers modules like random.

import random

print("They print random number b/w 1-10 :",random.randrange(1,11))

lst1 = [1, 2, 3, 4, 5]
print(random.choice(lst1))

lst2 = ["a","b","c","d"]
print(random.choice(lst2))

lst3 = [1, 2, 3, 4, 5,"a","b","c"]
print(random.choice(lst3))

random.shuffle(lst3)
print("After Shuffle is : ",lst3)