class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # TODO 未通过 error
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        if not prices: return 0
        k = 2
        dp = [[[0]*2] * (k+1)] * len(prices)
        for i in range(len(prices)):
            for j in range(k, 0, -1):
                # print(j)
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        print(dp)
        return dp[len(prices)-1][k][0]




        # if not prices:
        #     return 0
        # n = len(prices)
        # dp = [[0, 0] for _ in range(3)]
        # for i in range(0, n+1):
        #     for k in range(2, 0, -1):
        #         if i == 0:
        #             #dp[0][k][1] = -inf i=0不存在，
        #             #所以dp[0][k][1] + prices[i-1]必须小于dp[0][k][0]=0,
        #             #所以 dp[i-1][k][1]=-inf or = -price[i]
        #             dp[k][1] = float('-inf')
        #         else:
        #             dp[k][0] = max(dp[k][0], dp[k][1] + prices[i-1])
        #             dp[k][1] = max(dp[k][1], dp[k-1][0] - prices[i-1])
        # return max(0, dp[2][0])

