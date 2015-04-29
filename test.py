import os
from collections import *

linker = set()
with open('./connectives.csv', 'r', encoding = 'utf-8') as f:
    for l in f:
        temp = defaultdict(float)
        arg1, arg2, _, temp['a'], temp['b'], temp['c'], temp['d'] = l.rstrip().split(',')
        # print(max(temp.values()))
        if temp['c'] == max(temp.values()):
            # print("here")
            linker.add((arg1, arg2))
print(linker)

# a = [[1],[2],[3],[4],[5],[6]]
# temp = {tuple(l) for l in a}
# print(temp)
