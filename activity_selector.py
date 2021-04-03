def greedy_activity_selector(activities):
    length = len(activities)
    activities.sort(key=lambda x: x[1])
    result = [False] * length
    j = 0
    result[j] = True
    for i in range(1, length):
        if activities[i][0] >= activities[j][1]:
            j = i
            result[j] = True
    return result


def show(result):
    count = 0
    print('安排的活动为：')
    for i in range(len(result)):
        if result[i]:
            print('第', i + 1, '个活动')
            count += 1
    print('共有', count, '个活动！')


activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
res = greedy_activity_selector(activities)
show(res)
