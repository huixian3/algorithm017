'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
'''
import collections
class Solution(object):
    # 说明：暴力n^n算法，超出时间限制；单调栈复杂度n，效率较高


    # 最小栈
    def largestRectangleArea(self, heights):
        left, right = [], collections.deque()
        res = 0
        min_stack = []
        n = len(heights)
        for i in range(n):
            while min_stack and heights[min_stack[-1]] >= heights[i]:
                min_stack.pop()
            left.append(min_stack[-1] if min_stack else -1)
            min_stack.append(i)

        min_stack = []
        for i in range(n-1, -1, -1):
            while min_stack and heights[min_stack[-1]] >= heights[i]:
                min_stack.pop()
            right.appendleft(min_stack[-1] if min_stack else n)
            min_stack.append(i)
        # 遍历求遍历
        for i in range(n):
            s = (right[i] - left[i] - 1) * heights[i]
            res = max(res, s)
        return res

    # 左右边界遍历
    def largestRectangleArea(self, heights):
        n = len(heights)
        res = 0
        for l in range(n-1):
            h = heights[l]
            for r in range(l, n):
                h = min(h, heights[r])
                res = max(res, h * (r-l+1))
        return res


    # 遍历"高"
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        res = 0
        for i in range(n):
            l = i-1
            while l >= 0 and heights[l] >= heights[i]:
                l -= 1
            r = i+1
            while r < n and heights[r] >= heights[i]:
                r += 1
            res = max(res, (r-l-1) * heights[i])
        return res



    # 单调栈
    def largestRectangleArea(self, heights):
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
'''
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> left(n), right(n);
        
        stack<int> mono_stack;
        for (int i = 0; i < n; ++i) {
            while (!mono_stack.empty() && heights[mono_stack.top()] >= heights[i]) {
                mono_stack.pop();
            }
            left[i] = (mono_stack.empty() ? -1 : mono_stack.top());
            mono_stack.push(i);
        }

        mono_stack = stack<int>();
        for (int i = n - 1; i >= 0; --i) {
            while (!mono_stack.empty() && heights[mono_stack.top()] >= heights[i]) {
                mono_stack.pop();
            }
            right[i] = (mono_stack.empty() ? n : mono_stack.top());
            mono_stack.push(i);
        }
        
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, (right[i] - left[i] - 1) * heights[i]);
        }
        return ans;
    }
};


'''