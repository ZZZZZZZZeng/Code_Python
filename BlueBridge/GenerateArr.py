import random


# 使用random生成长度在[0,max_length)，每个元素在(-max_value,max_value]之间的数组
def generateArr(max_length, max_value):
    length = int(random.random() * max_length)

    arr = []
    for i in range(length):
        arr.append(random.random() * (max_value + 1) - random.random() * max_value)
    return arr

if __name__ == "__main__":
    print(generateArr(100,100))