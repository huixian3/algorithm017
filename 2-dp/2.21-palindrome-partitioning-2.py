class Solution(object):
    # 最小分割次数
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # dp = [[False]* n] * n
        # 判断回文串
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if j-i < 2: dp[i][j] = s[i] == s[j]
                else: dp[i][j] = dp[i+1][j-1] and s[i] == s[j]

        # min cut
        # t[i] 表示 i结尾的最小分割次数，可初始化为字符串长度
        # t[i] = min(t[i], dp[j+1][i]+1) if dp[j+1][i] else t[i]
        t = [i for i in range(n)]
        for i in range(1, n):
            # 无需分割
            if dp[0][i]:
                t[i] = 0
                continue
            for j in range(0, i):
                t[i] = min(t[i], t[j]+1) if dp[j+1][i] else t[i]
        return t[-1]