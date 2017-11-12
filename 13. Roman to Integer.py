class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        m = {'C': 100,'D': 500, 'I': 1, 'L': 50, 'M': 1000, 'V': 5, 'X': 10}
        for i in xrange(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i]]:
                res -= m[s[i]]
            else:
                res += m[s[i]]
        return res
