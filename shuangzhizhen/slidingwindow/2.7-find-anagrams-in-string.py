class Solution(object):
    def findAnagrams(self, s2, s1):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if not s2 or not s1 or len(s2) < len(s1): return res
        left, right = 0, 0

        need, window = collections.defaultdict(int), collections.defaultdict(int)
        for ch in s1: need[ch] += 1
        valid = 0

        # 扩大右侧窗口边界
        while right < len(s2):
            ch = s2[right]
            right += 1
            # 更新窗口数据
            if ch in need:
                window[ch] = window[ch] + 1
                if window[ch] == need[ch]: valid += 1

            print(str(left), str(right))
            # 改动1：判断左侧窗口是否需收缩
            while right - left >= len(s1):
                # 改动2：更新结果
                if valid == len(need):
                    res.append(left)
                # 左边界移动，移除一个元素
                l_ch = s2[left]
                left += 1
                # 更新窗口数据
                if l_ch in need:
                    if window[l_ch] == need[l_ch]: valid -= 1
                    window[l_ch] = window[l_ch] - 1
        return res