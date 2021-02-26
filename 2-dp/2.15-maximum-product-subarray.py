class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # dp_max[i]:表示以nums[i]结尾的乘积最大的子数组的乘积，dp_min[i]：表示以nums[i]结尾的乘积最小的子数组的乘积
        dp_max = nums[0]
        dp_min = nums[0]
        n = len(nums)
        res = dp_max
        for i in range(1, n):
            temp = dp_max
            dp_max = max(dp_max * nums[i], dp_min * nums[i], nums[i])
            dp_min = min(temp * nums[i], dp_min * nums[i], nums[i])
            res = max(res, dp_max)
        return res