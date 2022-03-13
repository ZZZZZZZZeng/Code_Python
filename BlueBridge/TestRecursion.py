import random


def generate_arr(max_length, max_value):
    # 生成一个 int value = max_length*[0,1)       random.random()
    length = int(random.random() * max_length)
    arr = []

    for i in range(length):
        # 在数组里面随机填数，两个random()值不一样
        arr.append(random.random() * (max_value + 1) - random.random() * max_value)

    return arr


def getMax(arr, l, r):
    if r == l:
        return arr[l]

    mid = l + (r - l) // 2
    maxleft = getMax(arr, l, mid)
    maxright = getMax(arr, mid + 1, r)
    return max(maxleft, maxright)


def rightMax(arr):
    return max(arr)


max_length = 100
max_value = 10000
test_time = 100

if __name__ == "__main__":
    right = True
    for test_time in range(test_time):
        # 生成测试数组
        arr = generate_arr(max_length, max_value)
        max1 = getMax(arr, 0, len(arr) - 1)
        max2 = rightMax(arr)
        # 如果不相等，那么打印出来，把right值改为false
        if not max1 == max2:
            print('max1', max1)
            print('max2', max2)
            right = False
    # 打印结果
    if right:
        print('right!')
    else:
        print('wrong!')
