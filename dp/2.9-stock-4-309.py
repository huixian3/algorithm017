class Solution(object):
    # 利润减去手续费即可
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # 使用变量dp_pre_0存储前天没有股票的利润，用于更新今天购买股票的利润
        if not prices: return 0
        n = len(prices)
        dp_0, dp_1 = 0, -prices[0]
        dp_pre_0 = 0
        for i in range(n):
            new_dp_0 = max(dp_0, dp_1 + prices[i])
            new_dp_1 = max(dp_1, dp_pre_0 - prices[i])
            dp_pre_0 = dp_0
            dp_0, dp_1 = new_dp_0, new_dp_1
        return dp_0

        # dp[i][0] = Math.max(dp[i - 1][0], dp[i-1][1] + prices[i]);
        # dp[i][1] = Math.max(dp[i - 1][1],  dp[i-2][0]- prices[i]);
        # TODO 该方法 error
        if not prices: return 0
        n = len(prices)
        dp = [[0]*2] * (n)
        dp[-1][0] = 0
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[0]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]- prices[i])
        return dp[n-1][0]


