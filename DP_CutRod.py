# 自顶向下
def CutRod(p, n):
    if n == 0:
        return 0
    q = -1  # 当前最大值
    for i in range(1, n + 1):
        q = max(q, p[i] + CutRod(p, n - i))
    return q


# 带备忘录的自顶向下
def MemorizedCutRod(p, n):
    r = [-1] * (n + 1)  # 保留每个子问题的解

    def MemorizedCutRodAux(p, n, r):
        if r[n] >= 0:
            return r[n]
        q = -1  # 当前最大值
        if n == 0:
            q = 0
        else:
            for i in range(1, n + 1):
                q = max(q, p[i] + MemorizedCutRodAux(p, n - i, r))
        r[n] = q
        return q

    return MemorizedCutRodAux(p, n, r), r


# 自底向上
def BottomUpCutRod(p, n):
    r = [0] * (n + 1)
    for i in range(1, n + 1):
        if n == 0:
            return 0
        q = 0
        for j in range(1, i + 1):
            q = max(q, p[j] + r[i - j])
            r[i] = q
    return r[n], r


# 扩展自底向上
def ExtendedBottomUpCutRod(p, n):
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        q = 0
        if n == 0:
            return 0
        for j in range(1, i + 1):
            if q < p[j] + r[i - j]:
                q = p[j] + r[i - j]
                s[i] = j
        r[j] = q
    return r, s


# 只能计算0~10的最大收益
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# print('最大收益为：', CutRod(p, 10))
print('最大收益为：', ExtendedBottomUpCutRod(p, 10))
