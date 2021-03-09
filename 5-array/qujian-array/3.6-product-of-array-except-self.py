class Solution(object):
    # Q：给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
    # 不能用除法
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 当前数左边的乘积 * 当前数右边的乘积
        res = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        temp = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i] * temp
            temp *= nums[i]
        return res

        # 方法2：思路同方法1
        res, p, q = [1], 1, 1
        for i in range(len(nums) - 1): # bottom triangle
            p *= nums[i]
            res.append(p)
        for i in range(len(nums) - 1, 0, -1): # top triangle
            q *= nums[i]
            res[i - 1] *= q
        return res