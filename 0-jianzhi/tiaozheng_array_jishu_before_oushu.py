class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
        使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
        '''
        # 双指针
        if not nums: return nums
        n = len(nums)
        l, r = 0, 0
        while r < n:
            if nums[r] & 1 == 1:
                if l != r:
                    nums[l], nums[r] = nums[r], nums[l] # 不保序
                l += 1
            r += 1
        return nums

