class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 思路：贪心算法，每次将最小的饼干分配给胃口最小的孩子
        s.sort()
        g.sort()
        res = i = j = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res, i, j = res+1, i+1, j+1
            else:
                j = j+1
        return res

