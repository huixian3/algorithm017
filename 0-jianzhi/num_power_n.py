class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not x:
            return 0
        if n < 0:
            n, x = -n, 1/x
        res = 1
        while n:
            if n & 1 == 1:
                res *= x
            x *= x
            n >>= 1
        return res
