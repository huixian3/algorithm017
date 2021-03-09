class Solution(object):
    # Q: 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 1. 栈: 分层计算容积
        res = 0
        stack = []
        idx = 0
        while idx < len(height):
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0: break
                h = min(height[idx], height[stack[-1]]) - height[top]
                dist = idx - stack[-1] -1
                res += dist * h
            stack.append(idx)
            idx += 1
        return res

        # 2. 双指针
        n = len(height)
        l, r = 0, n-1
        res = 0
        left_max, right_max = 0, 0
        while l < r:
            if height[l] < height[r]:
                # change left
                if left_max < height[l]: left_max = height[l]
                else:
                    res += left_max - height[l]
                l += 1
            else:
                if right_max < height[r]: right_max = height[r]
                else:
                    res += right_max - height[r]
                r -= 1
        return res

        # 3. 暴力，存储左右最大边界
        left_max = []
        right_max = collections.deque()
        res = 0
        left = 0
        right = 0
        n = len(height)
        for i in range(n):
            if height[i] > left: left = height[i]
            left_max.append(left)
        for i in range(n-1, -1, -1):
            if height[i] > right: right = height[i]
            right_max.appendleft(right)
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i] if min(left_max[i], right_max[i]) > height[i] else 0
        return res



