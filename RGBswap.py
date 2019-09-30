###
# Coding Challenge #35
# 9/30/19
###

import time as t

def swap(letters):
    r_index = 0
    g_index = 0

    for i in range(0, len(letters)):
        letters[i].capitalize()
        if letters[i] is 'R':
            letters[i], letters[r_index] = letters[r_index], letters[i]
            if r_index + 1 < len(letters):
                r_index += 1
                g_index = r_index + 1
                # print("i: {} \nr_index: {} \ng_index: {}".format(i, r_index, g_index))

    for i in range(r_index+1, len(letters)):
        if letters[i] is 'G':
            letters[i], letters[g_index] = letters[g_index], letters[i]
            if g_index + 1 < len(letters):
                g_index += 1

    return letters


ex = ['R', 'G', 'G', 'B', 'R', 'B', 'B', 'R', 'R', 'G']
ex1 = ['G', 'G', 'G', 'B', 'B', 'R', 'R', 'G', 'G', 'B']

print("ex before", ex)
start = t.perf_counter()
print("ex after", swap(ex))
print('ex time: {}s'.format(t.perf_counter() - start))

print("ex1 before", ex1)
start = t.perf_counter()
print("ex1 after", swap(ex1))
print('ex1 time: {}s'.format(t.perf_counter() - start))
