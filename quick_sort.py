# 快速排序1
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    mid = arr[len(arr) // 2]
    left, right = [], []
    arr.remove(mid)
    for item in arr:
        if item >= mid:
            right.append(item)
        else:
            left.append(item)
    return quick_sort(left) + [mid] + quick_sort(right)


a = [1, 6, 4, 9, 2, 3, 8, 7, 5]
ret = quick_sort(a)
print(ret)

# 快速排序2
quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
    [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
    [item for item in array[1:] if item > array[0]])

ret2 = quick_sort([1, 6, 8, 4, 9, 2, 3, 7, 5])
print(ret2)


# 快速排序的随机化版本
def random_quicksort(A, left, right):
    if left < right:
        mid = random_partition(A, left, right)
        random_quicksort(A, left, mid - 1)
        random_quicksort(A, mid + 1, right)


import random


def random_partition(A, left, right):
    t = random.randint(left, right)
    A[right], A[t] = A[t], A[right]
    x = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1


A = [2, 8, 7, 1, 3, 5, 6, 4]
random_quicksort(A, 0, 7)
print(A)
