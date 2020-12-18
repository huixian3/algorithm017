class Solution:
    # 自底向上：dp数组的迭代
    def rob(self, nums):
        n = len(nums)
        if n<= 1:
            return nums[0] if nums else 0

        # memo=[0] * n
        first, second = nums[0], max(nums[0],nums[1])
        n = len(nums)
        for x in range(2, n):
            first, second = second, max(second, first + nums[x])
        return second

    def rob2(self, nums):
        n = len(nums)
        if n<= 1:
            return nums[0] if nums else 0

        memo=[0] * n
        memo[0], memo[1] = nums[0], max(nums[0],nums[1])
        n = len(nums)
        for x in range(2, n):
            memo[x] = max(memo[x-1], memo[x-2] + nums[x])
        return memo[-1]
    # 自顶向下: 带有备忘录的递归方法
    def rob1(self, nums):
        n = len(nums)
        if n<= 1:
            return nums[0] if nums else 0
        memo = {}
        return self.dp(n-1, nums, memo)

    def dp(self, i, nums, memo):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        if i in memo:
            return memo[i]
        memo[i] = max(self.dp(i-1,nums, memo) , self.dp(i-2,nums, memo) + nums[i])
        return memo[i]


print(Solution().rob([1,2,3,1,5,6,7,5,4,3,2]))