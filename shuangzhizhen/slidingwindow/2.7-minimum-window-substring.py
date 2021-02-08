import sys
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 滑动窗口
        # 1. 窗口边界初始化为0
        # 2. 右边界扩大，直到满足条件
        # 3. 左边界缩小，直到不满足条件
        if not s or not t or len(s) < len(t): return ""
        length, index = sys.maxsize, 0
        left, right = 0, 0

        need, window = collections.defaultdict(int), collections.defaultdict(int)
        for ch in t: need[ch] += 1
        valid = 0


        # 扩大右侧窗口边界
        while right < len(s):
            ch = s[right]
            right += 1
            # 更新窗口数据
            if ch in need:
                window[ch] = window[ch] + 1
                if window[ch] == need[ch]: valid += 1

            # print(str(left), str(right))
            # 判断左侧窗口是否需收缩
            while valid == len(need):
                # 更新结果
                if right - left < length: length, index = right-left, left
                # 左边界移动
                l_ch = s[left]
                left += 1
                # 更新窗口数据
                if l_ch in need:
                    if window[l_ch] == need[l_ch]: valid -= 1
                    window[l_ch] = window[l_ch] - 1
        return s[index:index + length] if length != sys.maxsize else ""



print(Solution().minWindow("ADOBECODEBANC", "ABC"))

