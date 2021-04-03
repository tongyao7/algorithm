# 区间[0,1)均匀分布的桶排序

import random


class bucket_sort(object):
    def _max(self, oldlist):
        _max = oldlist[0]
        for i in oldlist:
            if i > _max:
                _max = i
        return _max

    def _min(self, oldlist):
        _min = oldlist[0]
        for i in oldlist:
            if i < _min:
                _min = i
        return _min

    def sort(self, oldlist):
        _max = self._max(oldlist)
        _min = self._min(oldlist)
        s = [0 for i in range(_min, _max + 1)]
        for i in oldlist:
            s[i - _min] += 1  # 初始化桶
        current = _min
        n = 0
        for i in s:  # [current:i]
            while i > 0:
                oldlist[n] = current
                i -= 1
                n += 1
            current += 1  # 当前值

    def __call__(self, oldlist):
        self.sort(oldlist)
        return oldlist


a = [random.randint(0, 100) for i in range(10)]
bucket_sort()(a)
print(a)