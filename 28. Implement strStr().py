class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1, l2 = len(haystack), len(needle)
        if l2 > l1:
            return -1
        for i in xrange(l1 - l2 + 1):
            if haystack[i: i + l2] == needle:
                return True
        return False
    # O(k*(n - k)), O(1)