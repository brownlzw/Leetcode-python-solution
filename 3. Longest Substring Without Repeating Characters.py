class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        i = 0
        max_len = 0
        for j, char in enumerate(s):
            if char in m:
                i = max(i, m[char] + 1)
            m[char] = j
            max_len = max(max_len, j - i + 1)
        return max_len
    # O(n), O(n)

        m = {}
        i, max_len = 0, 0
        for j, c in enumerate(s):
            if c in m:
                if j - i > max_len:
                    max_len = j - i
                if m[c] + 1 > i:
                    i = m[c] + 1
            m[c] = j
        if len(s) - i > max_len:
            max_len = len(s) - i
        return max_len

