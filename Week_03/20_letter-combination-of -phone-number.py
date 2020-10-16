class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 暴力方法，n层循环
        # 递归
        result = []
        dic = {'2':'abc','3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def travese(l, n, res):
            if l == n:
                return result.append(''.join(res)) if n else []
            # 处理当前层
            val = dic[digits[l]]
            for ch in val:
                travese(l+1, n, res + [ch])
        travese(0, len(digits), [])
        return result