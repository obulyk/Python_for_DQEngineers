import string
import random
global res
global l
def randomList():
    l = []
    randomNumberOfList = random.randint(2, 10)
    for i in range(randomNumberOfList):
        tple = {random.choice(string.ascii_lowercase): random.randint(0, 100),
                random.choice(string.ascii_lowercase): random.randint(0, 100),
                random.choice(string.ascii_lowercase): random.randint(0, 100)}
        l.append(tple)
    return l
[{'c': 65, 'w': 0, 'l': 7}, {'v': 60, 'f': 79, 'o': 72}, {'z': 7, 'g': 61, 'l': 77}]
def sameNamebutDiffvalues(l):
    from collections import defaultdict
    global res
    res = defaultdict(list)
    for sub in l:
        for key in sub:
            res[key].append(sub[key])
            res.get(key)
    print('Concantenated list: '+str(dict(res)))
    return res
{'c': [65], 'w': [0], 'l': [7, 77], 'v': [60], 'f': [79], 'o': [72], 'z': [7], 'g': [61]}
def sameNamebutDiffvalues(res):
    commonDictionary = {}
    for key, value in res.items():
        if len(value) > 1:
            commonDictionary.update({key + str('_') + str(value.index(max(value)) + 1): max(value)})
        else:
            commonDictionary.update({key: max(value)})
    return (print('Common dictionary:', commonDictionary))
sameNamebutDiffvalues({'c': [65], 'w': [0], 'l': [7, 77], 'v': [60], 'f': [79], 'o': [72], 'z': [7], 'g': [61]})
