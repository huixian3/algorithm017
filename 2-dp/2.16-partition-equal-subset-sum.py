class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dp[i][j] = 前i+1个元素，是否可以选出一个和为j的子集, return bool
        # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        n = len(nums)
        if n <= 1: return False
        s = sum(nums)
        if s & 1 == 1: return False
        target = s >> 1
        print(target)
        # dp1 = [[False] * (target + 1)] * n
        dp = [[False for _ in range(target+1)] for _ in range(len(nums))]
        if nums[0] <= target: dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(target+1):
                if j-nums[i] > 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n-1][target]
