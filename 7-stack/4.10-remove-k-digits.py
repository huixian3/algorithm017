'''
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。

'''
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # 最小栈，最多移除k位
        n = len(num)
        if n <= k: return '0'
        stack = []
        remain = n - k
        for ch in num:
            while k > 0 and stack and stack[-1] > ch :
                stack.pop()
                k -= 1
            stack.append(ch)
        return ''.join(stack[:remain]).lstrip('0') or '0'



