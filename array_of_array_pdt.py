# inp: arr = [2,7,3,4]
# op: [84, 24, 56, 42]

import functools
import operator


arr = [2,7,3,4]
mult = []
for index in range(len(arr)-1):
    next_list_pdt = functools.reduce(operator.mul, arr[index+1:])
    if not index:
        prev_list_pdt = 1
    else:
        prev_list_pdt = functools.reduce(operator.mul, arr[:index])
    mult.append(next_list_pdt*prev_list_pdt)
mult.append(functools.reduce(operator.mul, arr[:-1]))
print(mult)
