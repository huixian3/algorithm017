class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]

        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 0:
                    if i >= 1 and j>= 1:
                        f[i][j] = f[i - 1][j] + f[i][j - 1]
                    # 处理边界条件
                    elif i >= 1:
                        f[i][j] = f[i - 1][j]
                    elif j >= 1:
                        f[i][j] = f[i][j-1]
                else:
                    f[i][j] = 0
        return f[m - 1][n - 1]

    # 从0开始递推
    def uniquePathsWithObstacles2(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [1] + [0]*m
        for i in range(0, n):
            for j in range(0, m):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j]+dp[j-1]
        return dp[-2]



# print(Solution().uniquePaths(4,5))
print(Solution().uniquePathsWithObstacles2([[1,0]]))