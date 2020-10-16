class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 回溯法 逐层尝试，if ok goon or save，else godie
        def nqueens(row, col_list, xy_sum, xy_diff):
            # 终止条件
            if row == n and len(col_list) == n:
                result.append(['.'* (i) + 'Q' +'.' * (n-i-1) for i in col_list])
                return
            # 逐列尝试
            for col in range(n):
                # 处理当前层, 避免冲突
                if col+row not in xy_sum and col-row not in xy_diff and col not in col_list:
                    # 下探到下一层
                    nqueens(row+1, col_list + [col], xy_sum + [col+row], xy_diff + [col - row])
                    # reverse
        result = []
        nqueens(0,[],[],[])
        return result