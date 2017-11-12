class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        end = 0
        for i in xrange(len(strs[0])):
            cur = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != cur:
                    return s[:i]
        return strs[0]
