class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 从右上角开始，if >target： 向左移；if <target
        if not matrix:
            return False

        n = len(matrix)
        m = len(matrix[0])
        i, j = 0, m-1
        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j = j - 1
            elif matrix[i][j] < target:
                i = i + 1
        return False