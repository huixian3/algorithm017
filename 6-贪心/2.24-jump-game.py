class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 贪心 2
        # 从后往前，看 算法训练营

        # 贪心 1
        # 贪心的记录从0 到i-1的位置能跳到的最远位置most, 然后判断位置i，如果most<i说明无法跳到位置i。
        # most = max(most, i + nums[i])
        n = len(nums)
        most = 0
        for i in range(n):
            if most < i:
                return False
            most = max(most, i + nums[i])
        return True # 跳到了最后


