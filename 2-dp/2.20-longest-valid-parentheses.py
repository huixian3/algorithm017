class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i] 表示以i结尾的最长有效括号数

        """
        if s[i] == ')' and s[i-1] == '(':
            dp[i] = dp[i-2] + 2
        else if s[i] == ')' and s[i-1] == ')' and i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
            dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
        """
        n = len(s)
        max_l = 0
        dp = [0 for _ in range(n+1)]
        # 递推公式
        for i in range(1, n):
            if s[i] == ')' and s[i-1] == '(':
                if i == 1: dp[i] = 2
                else: dp[i] = dp[i-2] + 2
            elif s[i] == ')' and s[i-1] == ')' and i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i-1] + dp[i-dp[i-1] - 2] + 2
            max_l = max(max_l, dp[i])
        return max_l
