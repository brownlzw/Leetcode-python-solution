class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        n = len(grid[0])
        dp = [0] + [float('inf')] * (n - 1)
        for row in grid:
            dp[0] += row[0]
            for i in xrange(1, n):
                if dp[i - 1] < dp[i]:
                    dp[i] = dp[i - 1] + row[i]
                else:
                    dp[i] += row[i]
        return dp[-1]