class Solution:
    # 自底向上：dp数组的迭代
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n<= 1:
            return nums[0] if nums else 0
        return max(self.rob2(n-1, nums[1:]), self.rob2(n-1, nums[:n-1]))

    def rob2(self, n, nums):
        if n<= 1:
            return nums[0] if nums else 0
        memo=[0] * n
        memo[0], memo[1] = nums[0], max(nums[0],nums[1])
        n = len(nums)
        for x in range(2, n):
            memo[x] = max(memo[x-1], memo[x-2] + nums[x])
        return memo[-1]



print(Solution().rob([1,2,3,1,5,6,7,5,4,3,2]))