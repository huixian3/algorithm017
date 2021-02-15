import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 贪心算法
        profit = 0
        initial = sys.maxsize
        for p in prices:
            if p > 0 and initial < p:
                profit += (p - initial)
            initial = p
        return profit

        # dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
        # dp[i][1] = Math.max(dp[i - 1][1],  dp[i-1][0]- prices[i]);
        if not prices: return 0
        n = len(prices)
        dp = [[0]*2] * (n)
        print(dp)
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[0]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]- prices[i])
        return dp[n-1][0]

        # 优化内存空间
        if not prices: return 0
        n = len(prices)
        dp_0, dp_1 = 0, -prices[0]
        for i in range(n):
            new_dp_0 = max(dp_0, dp_1 + prices[i])
            new_dp_1 = max(dp_1, dp_0 - prices[i])
            dp_0, dp_1 = new_dp_0, new_dp_1
        return dp_0

