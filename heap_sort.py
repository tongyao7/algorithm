class Heap():
    def Parent(self, i):
        if i % 2 == 0:
            return i // 2 - 1
        else:
            return i // 2

    def Left(self, i):
        return 2 * i + 1

    def Right(self, i):
        return 2 * i + 2

    def heapify(self, a, i, heap_size):
        largest = i
        l = self.Left(i)
        r = self.Right(i)

        if l < heap_size and a[l] > a[largest]:
            largest = l

        if r < heap_size and a[r] > a[largest]:
            largest = r

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.heapify(a, largest, heap_size)

        # build a maxheap

    def build_max_heap(self, a):
        heap_size = len(a)
        for i in range(heap_size // 2 - 1, -1, -1):
            self.heapify(a, i, heap_size)

    def heap_sort(self, a):
        heap_size = len(a)
        self.build_max_heap(a)
        for i in range(heap_size - 1, 0, -1):
            a[i], a[0] = a[0], a[i]
            heap_size -= 1
            self.heapify(a, 0, heap_size)


arr = [12, 11, 13, 5, 6, 7]
H = Heap()
# H.build_max_heap(arr)
# H.heap_sort(arr)

print('排序前：', arr)


# 最大优先队列的实现
class PriorityQ(Heap):
    def HeapMaximum(self, a):
        return a[0]

    # 去掉并返回具有最大关键字的元素
    def HeapExtractMax(self, a):
        heap_size = len(a)
        if heap_size > 0:
            max = a[0]
            a[0] = a[heap_size - 1]
            del a[heap_size - 1]
            self.heapify(a, 0, len(a))
            return max

    # 将a[i]处的关键字增加到key,然后重新调整堆
    def HeapIncreaseKey(self, a, i, key):
        if key < a[i]:
            print('new key is smaller than current one')
        else:
            a[i] = key
            while i > 0 and a[self.Parent(i)] < a[i]:
                a[i], a[self.Parent(i)] = a[self.Parent(i)], a[i]
                i = self.Parent(i)

    def MaxHeapInsert(self, a, key):
        a.append(-65535)
        heap_size = len(a)
        self.HeapIncreaseKey(a, heap_size - 1, key)


P = PriorityQ()
print('max:', P.HeapMaximum(arr))
print('extract max:', P.HeapExtractMax(arr))
P.HeapIncreaseKey(arr, 2, 30)
P.MaxHeapInsert(arr,100)
print(arr)
