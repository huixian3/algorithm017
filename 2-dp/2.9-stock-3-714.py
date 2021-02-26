class Solution(object):
    # 利润减去手续费即可
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # if not prices: return 0
        # n = len(prices)
        # dp = [[0]*2] * (n)
        # for i in range(n):
        #     if i == 0:
        #         dp[i][0] = 0
        #         dp[i][1] = -prices[0]-fee
        #     else:
        #         dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #         dp[i][1] = max(dp[i-1][1], dp[i-1][0]- prices[i]-fee)
        # return dp[n-1][0]

        if not prices: return 0
        n = len(prices)
        for i in range(n):
            if i == 0:
                dp_0 = 0
                dp_1 = -prices[0]-fee
            else:
                new_dp_0 = max(dp_0, dp_1 + prices[i])
                new_dp_1 = max(dp_1, dp_0 - prices[i]-fee)
                dp_0, dp_1 = new_dp_0, new_dp_1
        return dp_0