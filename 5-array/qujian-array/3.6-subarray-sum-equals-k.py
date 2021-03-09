# Q：给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 借助hash表记录 "和 s-k 出现的次数"，即为符合要求的连续数组的个数。
        # res += count(nums[0:i] - num[0:j] == k)
        mp = collections.defaultdict(int)
        mp[0] = 1
        s = 0
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            res += mp[s-k]
            mp[s] += 1
        return res







