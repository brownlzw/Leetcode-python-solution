class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = "^#" + "#".join(s) + "#$"
        l = len(temp)
        dp = [0] * l
        center, right = 1, 1
        maxl, maxi = 1, 0
        for i in xrange(1, l - 1):
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while temp[i + dp[i] + 1] == temp[i - dp[i] - 1]:
                dp[i] += 1
            if i + dp[i] > right:
                center, right = i, i + dp[i]
            if dp[i] > maxl:
                maxl = dp[i]
                maxi = (i - dp[i]) / 2
        return s[maxi:maxi + maxl]
