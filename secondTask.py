import random
import string

[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
randomNumberOfList = random.randint(2, 10)
lst = []

for i in range(2):
    value = random.randint(0, 10)
    randomLetter = random.choice(string.ascii_lowercase)
    tple = {random.choice(string.ascii_lowercase): random.randint(0, 10),
            random.choice(string.ascii_lowercase): random.randint(0, 10),
            random.choice(string.ascii_lowercase): random.randint(0, 10)}
    lst.append(tple)
print(lst)


