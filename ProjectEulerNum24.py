# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import time
start = time.time()

digits = [0,1,2,3,4,5,6,7,8,9]

permutations = []

def permute(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list]
    permutation = []
    for i in range(len(list)):
        m = list[i]
        remaining_chars = list[:i] + list[i+1:]
        for k in permute(remaining_chars):
            permutation.append([m] + k)
    return permutation

permutations.append(permute(digits))

answer = permutations[0][999999]
print(*answer, sep='')

stop = time.time()
print('Time: ', stop - start)