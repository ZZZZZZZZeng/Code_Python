s = "dvdf"


# def lengthOfLongestSubstring(s):
#     length = len(s)
#     if length is None:
#         return 0
#     if s.count(s[0]) == length:
#         return 1
#     p1 = 0
#     p2 = 1
#     max = 0
#     while p2 < length:
#         if s[p2] not in s[p1:p2]:
#             p2 += 1
#             max = max if max > p2 - p1 else p2 - p1
#         else:
#             p1 = p1+1
#             p2 = p1 + 1
#     return max

def lengthOfLongestSubstring( s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 哈希集合，记录每个字符是否出现过
#         occ = set()
#         n = len(s)
#         # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
#         rk, ans = -1, 0
#         for i in range(n):
#             if i != 0:
#                 # 左指针向右移动一格，移除一个字符
#                 occ.remove(s[i - 1])
#             while rk + 1 < n and s[rk + 1] not in occ:
#                 # 不断地移动右指针
#                 occ.add(s[rk + 1])
#                 rk += 1
#             # 第 i 到 rk 个字符是一个极长的无重复字符子串
#             ans = max(ans, rk - i + 1)
#         return ans
#

#
# s = Solution()
l=lengthOfLongestSubstring(s)
# l1 = s.lengthOfLongestSubstring(s)
print(l)