# 最长公共子序列，c表示LCS的长度，b表示选择的子问题最优解

import numpy as np


def lcs(s1, s2):  # 运行时间O(len1*len2)
    len1 = len(s1)
    len2 = len(s2)
    c = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]  # shape:len1*len2
    b = [[-1 for i in range(len2 + 1)] for j in range(len1 + 1)]  # shape:len1*len2
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = '↖'  # 向左上走
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = '↑'  # 向上走
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = '←'  # 向左走
    return c, b, c[-1][-1]


def print_lcs(b, X, i, j):  # 运行时间O(len1+len2)
    if i == 0 or j == 0:
        return
    if b[i][j] == '↖':
        print_lcs(b, X, i - 1, j - 1)
        print(X[j - 1])
    elif b[i][j] == '↑':
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)


X1, X2 = 'ABCBDAB', 'BDCABA'
r, b, r2 = lcs(X1, X2)
print(np.array(b))
print('最长公共子序列的长度为：', r2)
print_lcs(b, X2, 7, 6)
