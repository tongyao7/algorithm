# 从一个无序的数组中求出第k大的数
# 随机选择算法，返回数组A[p...r]中第i小的元素

import random


def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i)


# 随机选择主元
def randomized_partition(A, p, r):
    pivot = random.randint(p, r)
    A[pivot], A[p] = A[p], A[pivot]

    temp = A[p]
    while p < r:
        while p < r and A[r] > temp:
            r -= 1
        A[p] = A[r]
        while p < r and A[p] <= temp:
            p += 1
        A[r] = A[p]
    A[p] = temp
    return p


A = [2, 8, 7, 1, 3, 5, 6, 4]
k = randomized_select(A, 0, 7, 3)
print(k)
print(A)
