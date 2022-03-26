# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import random


class Solution():

    # 解1：暴力破解,两个遍历找到 O(N^2)
    def twoSum0(self, nums, target):
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # 解2：荷兰国旗解法
    def twoSum(self, nums, target):
        nums.append(target)
        p1 = -1
        index = 0
        while index < len(nums) - 1:
            if nums[index] <= nums[len(nums) - 1]:
                p1 += 1
                nums[p1], nums[index] = nums[index], nums[p1]
                index += 1
            else:
                index += 1

        self.fastSort(nums, 0, p1)
        p0 = 0
        while p0 < p1:
            print(nums)
            print(p0,p1)
            print(nums[p0] , nums[p1])
            if nums[p0] + nums[p1] < target:
                p0 += 1
            elif nums[p0] + nums[p1] > target:
                p1 -= 1
            else:
                return [p0, p1]

    def fastSort(self, arr, l, r):
        # 在这里只接考虑 l<r 才进行计算（也就是说至少有2个数）,其他情况直接return
        if l < r:
            # 随机将数组中一个数放在数组的最右侧,
            # 仅仅是值发生了改变，数组坐标不发生变化
            self.swap(arr, l + int((r - l + 1) * random.random()), r)
            partition = self.getPartition(arr, l, r)
            self.fastSort(arr, l, partition[0] - 1)
            self.fastSort(arr, partition[1] + 1, r)

    def getPartition(self, arr, l, r):
        # 这里p2作为大于部分的起始位置，与小于部分原理类似
        # 因为表示位置的指针都在需要处理数组的外面
        # l为轮询的指针，r为比较基数的指针，l会在while循环内变化，而r则是跟随递归变化
        p1 = l - 1
        p2 = r
        while l < p2:
            if arr[l] < arr[r]:
                p1 += 1
                self.swap(arr, l, p1)
                l += 1
            elif arr[l] > arr[r]:
                p2 -= 1
                self.swap(arr, p2, l)
            else:
                l += 1
        self.swap(arr, p2, r)
        # 返回等于部分的头指针与尾指针p2之所以为尾指针，是因为p2与末尾的基数交换了位置
        return [p1 + 1, p2]

    def swap(self, arr, a, b):
        if a == b:
            return
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

if __name__ == "__main__":
    s=Solution()
    nums = [3,2,4]
    target = 6
    print(s.twoSum0(nums,target))
    print(s.twoSum(nums,target))