class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * (m - 1)
        for j in xrange(n):
            dp[0] = dp[0] and (1 - obstacleGrid[0][j])
            for i in xrange(1, m):
                if not obstacleGrid[i][j]:
                    dp[i] += dp[i - 1]
                else:
                    dp[i] = 0
        return dp[-1]