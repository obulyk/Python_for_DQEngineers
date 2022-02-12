from collections import defaultdict
import random
import string
l = []
randomNumberOfList = random.randint(2, 10)
for i in range(randomNumberOfList):
    tple = {random.choice(string.ascii_lowercase): random.randint(0, 100),
            random.choice(string.ascii_lowercase): random.randint(0, 100),
            random.choice(string.ascii_lowercase): random.randint(0, 100)}
    l.append(tple)
commonDictionary = {}
res = defaultdict(list)
for sub in l:
    for key in sub:
        res[key].append(sub[key])
        res.get(key)
print(dict(res))
for key, value in res.items():
    if len(value) > 1:
        commonDictionary.update({key + str('_') + str(value.index(max(value)) + 1): max(value)})
    else:
        commonDictionary.update({key: max(value)})
print('Common dictionary:', commonDictionary)