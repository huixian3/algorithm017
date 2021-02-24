class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i][j] 标识子串i-j中最长回文子序列长度
        # dp[i][j] =
        #     if s[i] != s[j]:
        #         max(dp[i+1][j], dp[i][j-1])
        #     else:
        #         max(dp[i][j], dp[i+1][j-1] + 2)
        # 边界条件：
        #     if j-i < 2
        #         dp[i][j] = j-i+1 if s[i]==s[j] else 0
        n = len(s)
        dp = [ [0 for raw in range(n)] for col in range(n) ]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2 if j-i > 1 else 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]


        # n = len(s)
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        # for i in range(n-1, -1, -1):
        #     for j in range(i, n):
        #         if j-i < 2:
        #             dp[i][j] = j-i+1 if s[i]==s[j] else 0
        #         else:
        #             if s[i] != s[j]:
        #                 dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        #             else:
        #                 dp[i][j] = max(dp[i][j], dp[i+1][j-1] + 2)
        # return dp[0][n-1]



