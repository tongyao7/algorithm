def radix_sort(a):
    i = 0  # 初始为个位排序
    n = 1  # 最小的位数置为1
    max_num = max(a)
    while max_num >= 10 ** n:
        n += 1
    print(n)
    while i < n:
        bucket = {}  # 用字典构建桶
        for x in range(10):
            bucket.setdefault(x, [])
        for x in a:
            radix = int((x / (10 ** i)) % 10)
            bucket[radix].append(x)
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:
                for y in bucket[k]:
                    a[j] = y
                    j += 1
        i += 1


a = [12, 3, 45, 3543, 214, 1, 4553]
radix_sort(a)
print(a)
