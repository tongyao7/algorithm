# 运行时间O(n^3)
def matrix_chain_order(p):
    n = len(p) - 1  # 矩阵个数
    m = [[0 for i in range(n)] for j in range(n)]  # m[n][n]保存m[i,j]的代价
    s = [[0 for i in range(n)] for j in range(n)]  # s[n][n]保存m[i,j]时取得最优代价处k的值
    for l in range(1, n):  # 控制列，从左往右
        for i in range(l - 1, -1, -1):  # 控制行，从下往上
            m[i][l] = float('inf')
            for k in range(i, l):
                q = m[i][k] + m[k + 1][l] + p[i] * p[k + 1] * p[l + 1]  # 第i个矩阵的行，第k个矩阵的列，第l个矩阵的列
                if q < m[i][l]:
                    m[i][l] = q  # 最优代价
                    s[i][l] = k  # 最优分割点
    return m, s


def print_option_parens(s, i, j):
    if i == j:  # 此时只含一个矩阵
        print('A' + str(i + 1), end='')
    else:  # 需要找一个k值，使m[i,j]=min{m[i,k]+m[k+1,j]+pi-1pkpj}
        print('(', end='')
        print_option_parens(s, i, s[i][j])
        print_option_parens(s, s[i][j] + 1, j)
        print(')', end='')


p = [30, 35, 15, 5, 10, 20, 25]  # 矩阵Ai的维数为pi-1pi,i=1,2,...,n
r, s = matrix_chain_order(p)
print(r)
print(s)
print_option_parens(s, 0, 5)
