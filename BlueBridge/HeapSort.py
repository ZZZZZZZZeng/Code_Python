# 自下往上形成最大堆（类似于给定数组形成最大堆，
# 每次从底部考虑一个数，逐步形成最大堆）
# 插入一个数调整代价O（logN）  也就是变动的层数（二叉树）
def heapInsert(arr, index):
    while arr[index] > arr[int((index - 1) / 2)]:
        arr[index], arr[int((index - 1) / 2)] = arr[int((index - 1) / 2)], arr[index]
        index = int((index - 1) / 2)


# 自上往下形成最大堆（类似于最大堆根结点出栈，然后剩下的部分形成最大堆）
# 向下落一个数调整代价O（logN）
def heapify(arr, index, heapSize):
    # 左孩子下标，但不知道是否有子孩子
    left = index * 2 + 1

    # 下方还有孩子,才继续往下落，否则就落到位了，退出函数
    while left < heapSize:
        # 两个孩子中，谁的值大，把下标给largest
        # !!!! 这里的判别条件不能写成     largest = left + 1 if arr[left] < arr[left+1] else left
        largest = left + 1 if arr[left + 1] > arr[left] and left + 1 < heapSize else left

        # 父亲和子孩子，谁的值大，把下标给largest
        largest = largest if arr[largest] > arr[index] else index

        # 父节点就是最大的值，所以不用往下走了，如果父节点不是最大的，则还要往下走
        if largest == index:
            break
        # 子节点是最大的值，和父节点交换位置，然后将index下移
        arr[largest], arr[index] = arr[index], arr[largest]
        index = largest
        left = index * 2 + 1


def heapSort(arr):  # O(Nlog(N))
    if arr is None or len(arr) < 2:
        return
    # 方法1 将原有数组变为一个大根堆
    # for i in range(len(arr)):
    #     heapInsert(arr, i)

    # 方法2 将原有数组变为一个大根堆
    # 从下往上，让每一个子树都是大根堆
    for i in range(len(arr), -1, -1):
        heapify(arr, i, len(arr))

    heapSize = len(arr) - 1
    arr[0], arr[heapSize] = arr[heapSize], arr[0]
    while heapSize > 0:  # O(N)
        heapify(arr, 0, heapSize)  # O(logN)
        heapSize -= 1
        arr[0], arr[heapSize] = arr[heapSize], arr[0]


if __name__ == "__main__":
    arr = [3, 5, 0, 3, 54, 6, 7, 87, 2]

    for index in range(len(arr)):
        heapInsert(arr, index)

    print(arr)
    print("------")
    arr[len(arr) - 1], arr[0] = arr[0], arr[len(arr) - 1]
    print(arr)
    print("------")
    heapify(arr, 0, len(arr) - 1)
    print(arr)
    print("------")
    for index in range(len(arr) - 1):
        heapInsert(arr, index)
    print(arr)
    print("------")
    heapSort(arr)
    print(arr)
