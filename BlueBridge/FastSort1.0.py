# 1.0 版本每次只会确定一个数，即最后那个比较的基数。
def fastSort(arr, l, r):
    # 在这里只接考虑 l<r 才进行计算（也就是说至少有2个数）,其他情况直接return
    if l < r:
        index = getIndex(arr, l, r)
        fastSort(arr, l, index - 1)
        fastSort(arr, index + 1, r)


def getIndex(arr, l, r):
    p1 = l - 1
    while l < r:
        if arr[l] <= arr[r]:
            p1 += 1
            swap(arr, l, p1)
            l += 1
        else:
            l += 1
    swap(arr, p1 + 1, r)
    return p1 + 1


def swap(arr, a, b):
    if a == b:
        return
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


if __name__ == "__main__":
    arr1 = [3, 5, 2, 7, 9, 1, 4, 6, 0, 8, 3, 4, 4, 3, 5, 3, 1, 2, 0, 5, 4, 7]
    fastSort(arr1, 0, len(arr1) - 1)
    print(arr1)
