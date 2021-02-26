#!/usr/bin/python3
# coding=utf-8

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1 or n < k:
            return list()
        result = []
        def back(res, l, k):
            if l == k:
                result.append(res)
            # 处理当前层
            i = 1 if not res else res[-1]
            while i <= n:
                if i not in res:
                    back(res+[i], l+1, k)
                i += 1
            #
        back([], 0, k)
        return result