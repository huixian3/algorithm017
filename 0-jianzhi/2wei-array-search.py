class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''
        每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
        [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]

        '''
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