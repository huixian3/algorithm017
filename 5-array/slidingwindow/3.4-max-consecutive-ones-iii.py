class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        nums0 = 0
        l, r = 0, 0
        res = 0
        while r < len(A):
            if A[r] == 0: nums0 += 1
            r += 1
            while nums0 > K:  # 注意边界条件
                if A[l] == 0: nums0 -= 1
                l += 1
            res = max(res, r-l)

        return res