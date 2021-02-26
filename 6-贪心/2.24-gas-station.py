class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 问题1：总油量是否大于消耗量
        # 问题2：从哪个点出发？ -从累积油量最少的 下一个点 出发
        if not gas or not cost or len(gas) != len(cost):
            return -1
        rest = 0
        min_rest = int(1e9)
        n = len(gas)
        for i in range(n):
            a = gas[i] - cost[i]
            rest += a
            if rest < min_rest:
                min_rest = rest
                pos = i
        if rest < 0: return -1
        return (pos+1) % n