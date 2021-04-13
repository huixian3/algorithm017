class Solution(object):
    # Q: 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    # 思路：每个位置的最大边界决定该位置，可容水量。选择左右最大边界较低的一支。

    def rainwater(self, height):
        # zhan
        stack = []
        res = 0
        for i in range(len(height)):
            # 直接添加
            if not stack or height[stack[-1]] > height[i]:
                stack.append(i)
            else:
                while height[stack[-1]] <= height[i]:
                    top = stack.pop()
                    h = min(height[top], height[i])
                    w = i-top-1
                    res += h*w
        return res




        # l, r = 0, len(height)-1
        # if r <= 0: return 0
        # max_l, max_r = height[0], height[-1]
        # res = 0
        # while l < r:
        #     if height[l] <= height[r]:
        #         # 更新左边
        #         if max_l > height[l]:
        #             res += max_l-height[l]
        #         else:
        #             max_l = height[l]
        #         l += 1
        #     else:
        #         # 更新右边
        #         if max_r > height[r]:
        #             res += max_r - height[r]
        #         else:
        #             max_r = height[r]
        #         r -= 1
        # return res


















    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 1. 栈: 分层计算容积
        # 用栈来跟踪可能储水的最长的条形块
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
        #
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



