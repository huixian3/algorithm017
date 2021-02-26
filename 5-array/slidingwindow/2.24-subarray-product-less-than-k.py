class Solution(object):
    '''
    给定一个正整数数组 nums。
    找出该数组内乘积小于 k 的连续的子数组的个数。
    '''
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 滑动窗口
        # 找到满足条件的，以索引i结束的子数组最大长度，相加
        if not nums: return 0
        left, right = 0, 0
        n = len(nums)
        # 记录[left:right+1]的乘积
        m = 1
        res = 0 # 记录子数组数量
        while right < n:
            # 窗口右侧扩充
            # 数据更新
            m *= nums[right]
            right += 1

            # 窗口左侧缩减
            while left < right and m >= k:
                # 数据更新
                m /= nums[left]
                left += 1
            if m < k:
                res += right-left
        return res

