# encoding = utf8


class Solution:
    # 返回从小到大顺序的列表
    # 冒泡排序
    def bubble_sort(self, a: list) -> list:
        for i in range(0, len(a)):
            for j in range(0, len(a) - 1 - i):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a

    # 选择排序
    def select_sort(self, a: list) -> list:
        for i in range(0, len(a)):
            for j in range(i + 1, len(a)):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
        return a

    # 插入排序
    def insert_sort(self, a: list) -> list:
        for i in range(1, len(a)):
            for j in range(i - 1, -1, -1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a

    # 快速排序
    def quick_sort(self, a: list, low: int, high: int) -> list:
        if low < high:
            pivot = self.find_pivot(a, low, high)
            a = self.quick_sort(a, low, pivot - 1)
            a = self.quick_sort(a, pivot + 1, high)
        return a

    def find_pivot(self, a: list, low: int, high: int) -> int:
        tmp = a[low]
        while low < high:
            while low < high and tmp < a[high]:
                high -= 1
            a[low] = a[high]
            while low < high and a[low] < tmp:
                low += 1
            a[high] = a[low]
        a[low] = tmp
        return low

    # 希尔排序
    def shell_sort(self, a: list) -> list:
        gap = int(len(a) / 2)  # 初始步长
        while gap > 0:
            # 插入排序
            for i in range(gap, len(a)):
                j = i
                while j >= gap and a[j - gap] > a[j]:
                    a[j - gap], a[j] = a[j], a[j - gap]
            gap = int(gap / 2)
        return a

    # 归并排序
    def merge_sort(self, a: list, low: int, high: int) -> list:
        if low < high:
            mid = int((low + high) / 2)
            a = self.merge_sort(a, low, mid)
            a = self.merge_sort(a, mid + 1, high)
            a = self.merge(a, low, mid, high)
        return a

    def merge(self, a: list, low: int, mid: int, high: int) -> list:
        len1 = mid - low + 1
        len2 = high - mid
        list1 = a[low:mid + 1]
        list2 = a[mid + 1:high + 1]

        i, j, k = 0, 0, low

        while i < len1 and j < len2:
            if list1[i] < list2[j]:
                a[k] = list1[i]
                i += 1
            else:
                a[k] = list2[j]
                j += 1
            k += 1

        while i < len1:
            a[k] = list1[i]
            i += 1
            k += 1
        while j < len2:
            a[k] = list2[j]
            j += 1
            k += 1

        return a


if __name__ == '__main__':
    object = Solution()
    a = [1, 8, 3, 5, 4, 7, 9, 0, 2, 6]
    a = object.merge_sort(a, 0, 9)
    print(a)
