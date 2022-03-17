# 自下往上形成最大堆
def heapInsert(arr, index):
    while arr[index] > arr[int((index - 1) / 2)]:
        arr[index], arr[int((index - 1) / 2)] = arr[int((index - 1) / 2)], arr[index]
        index = int((index - 1) / 2)


if __name__ == "__main__":
    arr1 = [3, 5, 2, 7, 9, 1, 4, 6, 0, 8, 3, 4, 4, 3, 5, 3, 1, 2, 0, 5, 4, 7, 0]
    for i in range(1, len(arr1)):
        heapInsert(arr1, i)
    print(arr1)
