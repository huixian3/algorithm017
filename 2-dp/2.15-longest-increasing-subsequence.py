class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 1
        # dp[i] 表示以nums[i]结尾的最大递增子序列长度
        # dp[i]=max(dp[j])+1, 其中 0≤j<i 且 num[j]<num[i]
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

