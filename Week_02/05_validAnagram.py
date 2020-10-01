#!/usr/bin/python3
# coding=utf-8

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        # 排序时间复杂度较高    char排序 and 比较
        # if sorted(s) != sorted(t):
        #     return False
        # else:
        #     return True

        # 时间复杂度O(n)  哈希表hashMap
        a = collections.defaultdict(int)
        for i in range(len(s)):
            a[s[i]] = a[s[i]] + 1
            a[t[i]] = a[t[i]] - 1
        for value in a.values():
            if value != 0:
                return False
        return True



