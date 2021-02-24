class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = nums[0]
        res = dp
        for i in range(1, n):
            dp = max(nums[i], dp + nums[i])
            res = max(dp, res)
        return res
