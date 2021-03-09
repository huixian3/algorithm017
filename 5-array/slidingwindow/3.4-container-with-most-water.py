class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        # 滑动窗口 左右边界短的往内移动
        l, r = 0, n-1
        res = 0
        while l < r:
            if height[l] <= height[r]:
                h = height[l]
                l += 1
            else:
                h = height[r]
                r -= 1
            w = r - l + 1
            res = max(res, h * w)
        return res


