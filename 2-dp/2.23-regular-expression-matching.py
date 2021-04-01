class Solution(object):
    '''
    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
    所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
    '''
    '''
    问题理解：p 需匹配所有s；且p可以有剩余元素。
    '''

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 是否匹配
        def match(i, j):
            if i == 0 or j == 0:
                return False
            if p[j-1] == '.':
                return True
            return p[j-1] == s[i-1]


        # dp[i][j] 表示 p的前j个元素 和 s的前i个元素是否匹配
        m, n = len(s), len(p)

        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == '*': #
                    dp[i][j] |= dp[i][j-2] # 如果i 和 j-1 不匹配，判断 j-2 是否能匹配i个元素
                    if match(i, j-1): # 如果i 和 j-1匹配，
                        dp[i][j] |= dp[i-1][j] # 因为* 能匹配多个字符，所以 只需满足j能匹配i-1即可
                else:
                    if match(i, j):
                        dp[i][j] = dp[i-1][j-1] #
        return dp[m][n]


