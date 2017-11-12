class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        if m > n:
            m, n = n, m
        dp = [1] * m
        for _ in xrange(1, n):
            for i in xrange(1, m):
                dp[i] += dp[i - 1]
        return dp[-1]
