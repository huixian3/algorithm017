class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 记录end表示的上次遍历区间[i, i+nums[i]]找到的最远位置，作为边界，当到达边界时更新，并将step+1
        # most表示遍历本次区间[i, i+nums[i]]能跳跃的最远位置
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step