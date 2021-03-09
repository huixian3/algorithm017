class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Q:给定一个包含 非负数 的数组和一个目标 整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，且总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。
        # 思路：子数组和可以整除k, sum[i:j+1] = pre_sum[j] - pre_sum[i]，也就是说：pre_sum[j]与pre_sum[i]如果除以k有相同的余数，则sum[i:j+1]就可以整除k
        # 前缀树
        mp = {0:-1}
        s = 0
        for i in range(len(nums)):
            s += nums[i]

            j = s if k == 0 else s%k
            if j not in mp:
                mp[j] = i
            else:
                if i - mp[j] > 1: return True
        return False