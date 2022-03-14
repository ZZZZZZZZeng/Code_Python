import random


def generate_arr(max_length, max_value):
    length = int(random.random() * max_length)

    arr = []
    for i in range(length):
        arr.append(random.random() * (max_value + 1) - random.random() * max_value)

    return arr


def mergesort(arr, l, r):
    # 无效值或者长度为0直接返回
    if l >= r:
        return 0

    mid = l + (r - l) // 2
    # merge是计算 当前 这个递归层的 小和数 ，而前面的mergesort则是下一个递归层的小和数
    return mergesort(arr, l, mid) + mergesort(arr, mid + 1, r) + merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    mergearr = []
    small_sum = 0
    left = l
    right = mid + 1
    while left <= mid and right <= r:
        if arr[left] <= arr[right]:
            small_sum += (r - right + 1) * arr[left]
            mergearr.append(arr[left])
            left += 1
        else:
            mergearr.append(arr[right])
            right += 1

    while left <= mid:
        mergearr.append(arr[left])
        left += 1

    while right <= r:
        mergearr.append(arr[right])
        right += 1

    for i in range(r - l + 1):
        arr[l + i] = mergearr[i]

    del mergearr
    return small_sum


# 对数器方法
def right_method(arr):
    smallsum = 0
    for i in range(len(arr)):
        small = 0
        for j in range(i):
            small += arr[j] if arr[j] < arr[i] else 0
        smallsum += small
    return smallsum


def right_method1(arr):
    smallsum = 0
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            smallsum += arr[j] if arr[j] < arr[i] else 0
    return smallsum


if __name__ == "__main__":
    # 定义测试参数
    max_length = 1000
    max_value = 10000
    test_time = 100
    right = True
    for test_time in range(test_time):
        # 生成arr1，并且copy一份
        arr1 = generate_arr(max_length, max_value)
        arr2 = arr1.copy()
        # 分别用两种方法计算小和
        smallsum1 = mergesort(arr1, 0, len(arr1) - 1)
        smallsum2 = right_method1(arr2)
        # 如果结果不相等（由于浮点数容易产生误差，这里取小于0.001即为相等），
        # 那么打印出来，把right赋值为false
        if not abs(smallsum1 - smallsum2) < 0.001:
            print("arr1:", arr1)
            print("arr2:", arr2)
            print('smallsum1', smallsum1)
            print('smallsum2', smallsum2)
            right = False
    # 打印结果
    if right:
        print('right!')
    else:
        print('wrong!')
