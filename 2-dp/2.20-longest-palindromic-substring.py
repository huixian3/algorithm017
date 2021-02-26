class Solution(object):
    # 最长回文子串
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # dp[i][j] 表示i-j是否为回文串
        # dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        # 其中 dp[i][i] = True, dp[i][i+1] = s[i]==s[i+1]

        n = len(s)
        if n <= 1: return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = s[0]
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
                res = s[i:j+1] if dp[i][j] and j-i+1 > len(res) else res

        return res
