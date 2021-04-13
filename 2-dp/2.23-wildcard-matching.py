class Solution(object):
    '''
    给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。
    '''
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j] 表示 j-1 个字母是否能匹配 i-1 个字符
        # 边界条件
        # dp[0][j] = True if *
        # dp[j][0] = False
        # dp[0][0] = True
        def match(i, j):
            if p[j] == '?': return True
            return s[i] == p[j]

        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        # 边界条件
        dp[0][0] = True
        # 处理 s='' p='**' ; dp[0][j]
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] if match(i-1, j-1) else False

        return dp[m][n]