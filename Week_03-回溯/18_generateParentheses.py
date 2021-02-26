#!/usr/bin/python3
# coding=utf-8
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 暴力 生成所有括号，之后判断合法性；左括号数量减去右括号数量>0，则合法
        # 递归：f(n) = ( f(0) ) f(n-1) + ( f(1) ) f(n-2) + ( f(2) ) f(n-3) + ...... + ( f(n-1) ) f(0)
        # 递归：将看成长度为n的格子，每个格子可以放左或右括号。
        #括号的合法性判断：左括号数量大于等于右括号数量
        def parentthesis(n, left, right, cur_str):
            # end
            if left == n and right == n:
                result.append(''.join(cur_str))

            # 处理当前层
            if left < n:
                parentthesis(n, left+1, right, cur_str + ['('])
            if left > right:
                parentthesis(n, left, right+1, cur_str + [')'])
            # 下砖下一层
            # reverse
        result = []
        parentthesis(n, 0, 0, [])
        return result

print(Solution.generateParenthesis(Solution, 6))
# def if __name__ == '__main__':
