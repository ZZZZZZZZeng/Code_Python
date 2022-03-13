import random


# 使用random生成长度在[0,max_length),每个元素在(-max_value,max_value]之间的数组
def generate_arr(max_length, max_value):
    length = int(random.random() * max_length)

    arr = []
    for i in range(length):
        arr.append(random.random() * (max_value + 1) - random.random() * max_value)

    return arr


# 归并排序
def mergesort(arr, l, r):
    # 无效值或者长度为0直接返回
    if l >= r:
        return
    mid = (l + r) // 2
    # 先排好左边和右边的，最后用merge整理成有序数组
    mergesort(arr, l, mid)
    mergesort(arr, mid + 1, r)
    merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    mergearr = []
    # 分别指带两边数组的头指针，这里不像java版本不需要辅助数组的指针，因为顺序填充append
    left = l
    right = mid + 1

    # 这里将两个排好序的子数组合并成为一个大的数组
    # 这里最终只会有一个子数组被完全拷贝到辅助数组
    # 而还有一个数组没有被拷贝完，因此要做额外的处理
    while left <= mid and right <= r:
        if arr[left] <= arr[right]:
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

    # 最后将辅助数组拷贝到原始的arr中
    for i in range(r - l + 1):
        arr[l + i] = mergearr[i]

    del mergearr


def right_sort(arr):
    arr.sort()
    return arr


# 定义数组相等的方法
def isequal(arr1, arr2):
    if arr1 is None and arr2 is None:
        return True
    if arr1 is None or arr2 is None:
        return False
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


# 定义测试参数
max_length = 1000
max_value = 1000
test_time = 1000
# right表示测试是否正确的标志
right = True

if __name__ == "__main__":
    for test_time in range(test_time):
        # 生成arr1，并且copy一份
        arr1 = generate_arr(max_length, max_value)
        arr2 = arr1.copy()
        # 分别用两种方法排序
        mergesort(arr1, 0, len(arr1) - 1)
        arr2 = right_sort(arr2)
        # 如果排序结果不相等，那么打印出来，把right赋值为false
        if not isequal(arr1, arr2):
            print('arr1', arr1)
            print("arr2", arr2)
            right = False
    if right:
        print('right!')
    else:
        print('wrong!')
