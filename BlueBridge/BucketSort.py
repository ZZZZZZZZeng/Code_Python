# 计算有几位数，计算斤桶的次数
def digit(arr):
    m_max = max(arr)
    result = 0
    while m_max != 0:
        result += 1
        m_max //= 10
    return result


# 获取最低位的数
def getDigit(x, d):
    return x // 10 ** (d - 1) % 10


# 桶相当于是一个队列，先进先出，
# 所以倒出来的时候，越后面的数字，越晚倒出来
def bucketSort(arr, l, r, digit):
    radis = 10
    i, j = 0, 0
    # 辅助数组
    bucket = [0] * radis
    # 进出桶的次数
    for d in range(1, digit + 1):
        # 初始化统计每一轮的词频数的列表
        count = [0] * radis
        # 统计词频数
        for i in range(l, r + 1):
            j = getDigit(arr[i], d)
            count[j] += 1

        # 统计分片词频数
        for i in range(1, radis):
            count[i] += count[i - 1]

        # 每一轮数据的排序
        for i in range(r, l - 1, -1):
            j = getDigit(arr[i], d)
            # 放在分片的末尾
            bucket[count[j] - 1] = arr[i]
            count[j] -= 1

        # 每一次排序完，都要将原有的数组做调整
        j = 0
        for i in range(l, r + 1):
            arr[i] = bucket[j]
            j += 1


if __name__ == "__main__":
    arr = [23, 14, 47, 71, 32,55555,66]
    bucketSort(arr, 0, len(arr) - 1, digit(arr))
    print(arr)