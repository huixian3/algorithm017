'''
拼接最大数
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

'''

# 核心：拆分问题
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 从一个数组中选 k 个数字，拼成最大数
        def pickK(nums, k):
            stack = []
            drop = len(nums) - k
            for ch in nums:
                while stack and drop and stack[-1] < ch:
                    stack.pop()
                    drop -= 1
                stack.append(ch)
            return stack[:k]
        # merge 两个数组，组成最大数
        def merge(A, B):
            stack = []
            while A or B:
                bigger = A if A > B else B
                stack.append(bigger[0])
                bigger.pop(0)
            return stack
        # 遍历所有情况，返回最大组合
        res = []
        for i in range(k+1):
            if i <= len(nums1) and k-i<= len(nums2):
                res = max(res, merge(pickK(nums1, i), pickK(nums2, k-i)) )
        return res


