def selectSort(arr):

    length = len(arr)
    if length < 2:
        return arr
    for i in range(length-1):
        temp = i
        for j in range(i+1, length):
            if arr[j] < arr[temp]:
                temp = j
        arr[temp], arr[i] = arr[i], arr[temp]

if __name__ == "__main__":
    arr1 = [3, 5, 2, 7, 9, 1, 4, 6, 0, 8, 3, 4, 4, 3, 5, 3, 1, 2, 0, 5, 4, 7,0]
    selectSort(arr1)
    print(arr1)