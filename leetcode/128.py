arr = []



def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    nums = set(nums)
    nums = list(nums)
    length = len(nums)
    nums.sort()
    i = 0
    j = i
    max = 1
    while i < length:
        if j+1 < length and nums[j] + 1 == nums[j+1]:
            j += 1
        elif j+1 == length:
            max = max if max >= j - i + 1 else j - i + 1
            return max
        else:
            max = max if max > j-i+1 else j-i+1
            i = j+1
            j = i
    return max

print(longestConsecutive(arr))
print(arr)