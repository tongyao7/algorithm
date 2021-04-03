def pack(w, v, C):
    dp = [[0 for j in range(C + 1)] for i in range(len(w) + 1)]
    for i in range(1, len(w) + 1):
        for j in range(1, C + 1):
            # 当前物品的重量超过了包的承载量，装不上，那它当前的最大价值就是原有包中的价值
            dp[i][j] = dp[i - 1][j]
            # 当前物品的重量没有包承载量大，可以装进去。 判断：装这个物品价值大还是不装这个物品价值大？从两种情况中选最大的。
            if j >= w[i - 1] and dp[i][j] < dp[i - 1][j - w[i - 1]] + values[i - 1]:
                dp[i][j] = dp[i - 1][j - w[i - 1]] + v[i - 1]
    return dp


def show(capicity, weights, dp):
    n = len(weights)
    print('最大价值：', dp[n][capicity])  # w和c最大时，价值最大
    x = [False for i in range(n)]
    j = capicity
    for i in range(n, 0, -1):
        if dp[i][j] > dp[i - 1][j]:  # 当相等时，没有装该物品
            x[i - 1] = True
            j -= weights[i - 1]
    print('背包中所装物品为：')
    for i in range(n):
        if x[i]:
            print('第{}个'.format(i + 1), end='')


n = 5
weights = [1, 2, 5, 6, 7]
values = [1, 6, 18, 22, 28]
capicity = 11

dp = pack(weights, values, capicity)
for i in range(len(dp)):
    print(dp[i])

# 输出要装的物品
show(capicity, weights, dp)
