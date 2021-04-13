'''
remove-duplicate-letters
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。
需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
'''

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 保证字典序，需要使用最小栈，同时栈中元素不能随意pop，原因是后续可能没有了
        # 1. 记录各元素出现次数
        # 2. 使用栈，判断元素是否要pop

        # 时间复杂度 O(N^N)
        dic = collections.Counter(s)
        stack = []
        for ch in s:
            if ch not in stack: # O(N)
                while stack and stack[-1] > ch and dic[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)

            dic[ch] -= 1
        return ''.join(stack)

        # 空间换时间，使用set，替换栈
        dic = collections.Counter(s)
        stack = []
        seen = set()
        for ch in s:
            if ch not in seen: # O(N)
                while stack and stack[-1] > ch and dic[stack[-1]] > 0:
                    seen.discard(stack.pop())
                stack.append(ch)
                seen.add(ch)
            dic[ch] -= 1
        return ''.join(stack)

