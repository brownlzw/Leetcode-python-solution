class Solution(object):
  def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    # dp = [[False] * (len(s) + 1) for i in range(len(p) + 1)]
    # dp[0][0] = True
    # for i in range(1, len(p)):
    #   dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
    # for i in xrange(len(p)):
    #   for j in xrange(len(s)):
    #     if p[i] == s[j] or p[i] == '.':
    #       dp[i + 1][j + 1] = dp[i][j]
    #     elif p[i] == '*':
    #       dp[i + 1][j + 1] = dp[i - 1][j + 1]
    #       if p[i - 1] == s[j] or p[i - 1] == '.':
    #         dp[i + 1][j + 1] |= dp[i][j + 1] or dp[i + 1][j]
    # return dp[-1][-1]

  # rcursive, using first match
  def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    return self.isMatch_v2(s, p, 0, 0, {})

  def isMatch_v2(self, s, p, i, j, memo):
    # check if s[i:] can be matched with p[j:]
    i_j_pair = (i, j)
    if i_j_pair not in memo:
      if j == len(p):
        match_result = i == len(s)
      else:
        first_match = i < len(s) and p[j] in [s[i], "."]
        if j < len(p) - 1 and p[j + 1] == "*":
          match_result = (first_match and self.isMatch_v2(s, p, i + 1, j, memo)) or self.isMatch_v2(s, p, i, j + 2,
                                                                                                    memo)
        else:
          match_result = first_match and self.isMatch_v2(s, p, i + 1, j + 1, memo)
      memo[i_j_pair] = match_result

    return memo[i_j_pair]