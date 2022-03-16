def insertSort(arr):
    length = len(arr)

    if length < 2:
        return arr

    # 打牌时第一张牌不需要比较大小，从第二张开始比较大小
    # 选择作比较的基数牌
    for i in range(1, length):
        # 从右向左看
        for j in range(i, 0, -1):
            # 直到比较基数的那张，不小于前面则停止
            if arr[j] >= arr[j - 1]:
                break
            else:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


if __name__ == "__main__":
    arr1 = [3, 5, 2, 7, 9, 1, 4, 6, 0, 8, 3, 4, 4, 3, 5, 3, 1, 2, 0, 5, 4, 7, 0]
    insertSort(arr1)
    print(arr1)
