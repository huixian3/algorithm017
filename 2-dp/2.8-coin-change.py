import sys
class Solution(object):
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 方法1：自底向上 使用 dp table; 完全背包问题
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1

        # 方法1：自底向上
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1+dp[i-coin])
        return dp[amount] if dp[amount] != float('inf') else -1


        # 方法2：自顶向下 递归dp，N叉树的 DFS遍历;
        memo = {} # 备忘录
        def dp(n):
            # print(self.res)
            if n in memo: return memo[n]
            res = sys.maxsize
            if n == 0: return 0
            if n < 0: return -1
            for coin in coins:
                sub = dp(n - coin)
                if sub == -1: continue
                res = min(1+sub, res)
            memo[n] = res if res != sys.maxsize else -1
            return memo[n]
        return dp(amount)



