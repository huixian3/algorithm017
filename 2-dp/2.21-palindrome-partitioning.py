class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 1. 找出所有回文子串； 2. 找所有可能分割方案
        # dp[i][j] 标识i-j 子串是否为回文串
        # dp[i][j] = dp[i+1][j-1] && s[i] == s[j]
        # 边界条件 j-i<2: dp[i][j] = s[i] == s[j]

        n = len(s)
        # dp = [[False]* n] * n
        # 判断回文串
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if j-i < 2: dp[i][j] = s[i] == s[j]
                else: dp[i][j] = dp[i+1][j-1] and s[i] == s[j]

        # 回溯找可用组合
        res = []
        def recur(i, cur):
            # end
            if i>=n: res.append(cur)
            #
            for j in range(i, n):
                if dp[i][j]:
                    recur(j+1, cur + [s[i:j+1]])
        recur(0, [])
        return res