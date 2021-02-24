class Solution(object):
    # 回文子串数量
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 1: return 1
        if n == 0: return 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = 0
        for i in range(n-1, -1, -1): # 该行必须逆序，否则dp[i+1][] 取值为False
            for j in range(i, n):
                # 边界1 处理
                if j == i:
                    dp[i][j] = True
                # 边界2
                elif j == i+1:
                    dp[i][j] = s[i]==s[j]
                # 状态转移方程
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j]: res += 1

        return res