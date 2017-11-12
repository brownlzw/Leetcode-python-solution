# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        while l <= h:
            mid = (l + h) / 2
            if isBadVersion(mid):
                if not mid or not isBadVersion(mid - 1):
                    return mid
                h = mid - 1
            else:
                l = mid + 1
        return l
