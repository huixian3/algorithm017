class Solution(object):
    # 最大正方形
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        """
        f[i][j] 表示由matrix[i-1][j-1]元素作为最右下角的最大正方形的边长。 返回 max(f[i][j]) * max(f[i][j])
                if i == 0 or j == 0:
                    f[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
        """
        m, n = len(matrix), len(matrix[0])
        f = [[0 for _ in range(n)] for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
                ans = max(ans, f[i][j])
        return ans * ans


