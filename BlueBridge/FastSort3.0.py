# 之所以1.0和2.0版本的时间复杂度都是O(N^2),
# 是因为不可避免最坏情况的发生，类似于9,8,7,6,5,4,3,2,2,1这样
# 3.0 版本则是在列表中随机选择一个数作为选择的基数，从而平均概率。
# 3.0 版本时间复杂度是O(NlogN)
import random


def fastSort(arr, l, r):
    # 在这里只接考虑 l<r 才进行计算（也就是说至少有2个数）,其他情况直接return
    if l < r:
        # 随机将数组中一个数放在数组的最右侧,
        # 仅仅是值发生了改变，数组坐标不发生变化
        swap(arr, l + int((r - l) * random.random()), r)
        partition = getPartition(arr, l, r)
        fastSort(arr, l, partition[0] - 1)
        fastSort(arr, partition[1] + 1, r)


def getPartition(arr, l, r):
    # 这里p2作为大于部分的起始位置，与小于部分原理类似
    # 因为表示位置的指针都在需要处理数组的外面
    # l为轮询的指针，r为比较基数的指针，l会在while循环内变化，而r则是跟随递归变化
    p1 = l - 1
    p2 = r
    while l < p2:
        if arr[l] < arr[r]:
            p1 += 1
            swap(arr, l, p1)
            l += 1
        elif arr[l] > arr[r]:
            p2 -= 1
            swap(arr, p2, l)
        else:
            l += 1
    swap(arr, p2, r)
    # 返回等于部分的头指针与尾指针p2之所以为尾指针，是因为p2与末尾的基数交换了位置
    return [p1 + 1, p2]


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
