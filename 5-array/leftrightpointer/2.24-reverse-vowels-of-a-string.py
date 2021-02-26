# reverse-vowels-of-a-string
class Solution(object):
    # 反转字符串中的元音字母
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 交换
        ss = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)
        if n <= 1: return s
        l, r = 0, n-1
        S = list(s)
        while l < r:
            while l < r and S[l] not in ss:
                l += 1
            while l < r and S[r] not in ss:
                r -= 1
            if l < r: S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1

        return ''.join(S)


