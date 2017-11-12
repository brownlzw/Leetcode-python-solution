class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        a, b = 1, 2
        for i in xrange(2, n):
            b, a = a + b, b
        return b