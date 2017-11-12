class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # i, j, match, star_index = 0, 0, 0, -1
        # while i < len(s):
        #   if j < len(p) and (s[i] == p[j] or p[j] == '*'):
        #     i += 1
        #     j += 1
        #   elif j < len(p) and p[j] == '*':
        #     star_index = j
        #     match = i
        #     j += 1
        #   elif star_index != -1:
        #     j = star_index + 1
        #     match += 1
        #     i = match
        #   else:
        #     return False
        # while j < len(p) and p[j] == '*':
        #   j += 1
        # return j == len(p)
        stars = p.count('*')
        if stars and stars == len(p):
            return True
        if len(p) - stars > len(s):
            return False
        dp = [False] + [True] * len(s)
        for c in p:
            if c == '*':
                for i in xrange(1, len(s) + 1):
                    dp[i] = dp[i] or dp[i - 1]
            else:
                for i in xrange(len(s) - 1, -1, -1):
                    dp[i + 1] = dp[i] and (c == s[i] or c == '?')
            dp[0] = dp[0] and c == '*'
        return dp[-1]
