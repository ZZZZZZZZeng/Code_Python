def bubbleSort(arr):
    length = len(arr)
    # 如果数组元素小于2，无需排序，直接返回
    if length < 2:
        return arr

    # 确定每一次遍历，所要确定的最终冒泡位置
    # N>=2 只有1-N位置上位置需要确定，0位置不用
    for i in range(length - 1, 0, -1):
        # 每次遍历比较的过程，从0开始到最终冒泡的前一个位置为止
        # 每次比较 j，j+1两个位置
        for j in range(i):
            if arr[j] > arr[j + 1]:
                #在python中支出如下的变量赋值
                # arr[i],arr[i + 1] = arr[i + 1],arr[i]
                swap(arr, j, j + 1)


def swap(arr, a, b):
    if a == b:
        return
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

if __name__ == "__main__":
    arr1 = [3, 5, 2, 7, 9, 1, 4, 6, 0, 8, 3, 4, 4, 3, 5, 3, 1, 2, 0, 5, 4, 7]
    bubbleSort(arr1)
    print(arr1)