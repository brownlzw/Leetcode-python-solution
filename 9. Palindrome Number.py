class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x /= 10
        return y == x or y / 10 == x