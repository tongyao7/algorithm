import random


def ramdom_self(a, b):
    x2 = bin(b).replace('0b', '')
    while (1):
        r = '0b'
        for i in range(len(x2)):
            m = random.randint(0, 1)  # 包括0，1
            r = r + str(m)
        final = eval(r)
        if final >= a and final <= b:
            return final


for i in range(20):
    print(ramdom_self(1, 8))

# --------------random algorithm--------------------------
import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(list)
print(list)


# 随机排列数组
def permute_by_sorting(a):
    permute_list = []
    n = len(a)
    for i in range(0, n):
        permute_list.append(random.randint(1, n ** 3))
    print(permute_list)
    for i in range(0, n):
        for j in range(i + 1, n):
            if permute_list[j] < permute_list[i]:
                permute_list[i], permute_list[j] = permute_list[j], permute_list[i]
                a[i], a[j] = a[j], a[i]


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
permute_by_sorting(list)
print(list)


# ---------------------------------------------------

# 概率随机抽奖

class randomMachine():
    def setWeight(self, weight):
        self.weight = weight
        self.chanceList = []
        for k, v in self.weight.items():
            for t in range(v):
                self.chanceList.append(k)

    def drawing(self):
        r = random.randrange(0, len(self.chanceList))
        print('随机数：', r)
        print(self.chanceList.pop(r))


test = randomMachine()
test.setWeight({'一等奖': 1, '二等奖': 1, '三等奖': 1, '安慰奖': 6})
for i in range(9):
    test.drawing()