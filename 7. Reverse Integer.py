class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1 * self.reverse(-x)
        res = 0
        while x:
            cur = x % 10
            if res > (2 ** 31 - 1) / 10 or res * 10 > 2 ** 31 - 1 - cur:
                return 0
            res = res * 10 + cur
            x /= 10
        return res