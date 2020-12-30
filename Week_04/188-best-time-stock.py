import sys
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 思路1：贪心，只要后面大于前面值，则把大于的部分加起来
        profit = 0
        initial = sys.maxsize
        for p in prices:
            if p > 0 and initial < p:
                profit += p - initial
            initial = p
        return profit