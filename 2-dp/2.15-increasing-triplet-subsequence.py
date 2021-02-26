import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3: return False
        # first and second 分别代表最小值和中间值，遇到小于first的值既替掉first，遇到小于second的值替掉second，遇到大于second的值，则说明这样的三元组存在。
        # 该方法只能判断是否存在递增三元组，并不能找到这样的三元组
        first, second = nums[0], sys.maxint
        for i in range(1, n):
            if nums[i] > second: return True
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] < second:
                second = nums[i]
        return False


        # dp 找到递增子序列，并判断长度大于3
        # if not nums:
        #     return 0
        # res = 1
        # # dp[i] 表示以nums[i]结尾的最大递增子序列长度
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #     if dp[i] >= 3:
        #         return True
        # return False