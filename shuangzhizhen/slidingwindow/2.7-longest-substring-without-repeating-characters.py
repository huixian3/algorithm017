class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 双指针：i 和 j 判断是否不含有重复 n*n

        # 滑动窗口1
        max_len = 0
        tb = []
        for c in s:
            while c in tb:
                del(tb[0])
            tb.append(c)
            max_len = max_len if len(tb) < max_len else len(tb)
        return max_len

        # 滑动窗口2
        if not s: return 0
        left, right = 0, 0
        length = -1
        tb = []
        # 扩大右侧窗口边界
        while right < len(s):
            ch = s[right]
            right += 1

            # 改动1：判断左侧窗口是否需收缩
            while ch in tb:
                # 改动2：更新窗口数据
                # 左边界移动，移除一个元素
                del(tb[0])
                left += 1
            # 更新窗口数据
            tb.append(ch)
            length = length if length > right-left else right - left

        return length