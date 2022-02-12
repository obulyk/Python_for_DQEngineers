l = []
def randomList():
    import string
    import random

    randomNumberOfList = random.randint(2, 10)
    for i in range(randomNumberOfList):
        tple = {random.choice(string.ascii_lowercase): random.randint(0, 100),
                random.choice(string.ascii_lowercase): random.randint(0, 100),
                random.choice(string.ascii_lowercase): random.randint(0, 100)}
        l.append(tple)
    return print(l)
def sameNamebutDiffvalues():
    randomList()
    from collections import defaultdict
    global res
    res = defaultdict(list)
    for sub in l:
        for key in sub:
            res[key].append(sub[key])
            res.get(key)
    print('Concantenated list: '+str(dict(res)))
    return res
def maxValue():
    sameNamebutDiffvalues()
    commonDictionary = {}
    for key, value in res.items():
        if len(value) > 1:
            commonDictionary.update({key + str('_') + str(value.index(max(value)) + 1): max(value)})
        else:
            commonDictionary.update({key: max(value)})
    return (print('Common dictionary:', commonDictionary))
maxValue()