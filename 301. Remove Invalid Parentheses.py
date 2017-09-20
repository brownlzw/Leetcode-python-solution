class Solution(object):
  def removeInvalidParentheses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    res = []
    self.remove(s, res, 0, 0, ['(', ')'])
    return res

  def remove(self, s, res, last_i, last_j, pair):
    count = 0
    for i in range(last_i, len(s)):
      count += (s[i] == pair[0]) - (s[i] == pair[1])
      if count < 0:
        for j in range(last_j, i + 1):
          if s[j] == pair[1] and (j == last_j or s[j - 1] != pair[1]):
            self.remove(s[:j] + s[(j + 1):], res, i, j, pair)
        return None
    s = s[::-1]
    if pair[0] == '(':
      self.remove(s, res, 0, 0, [')', '('])
    else:
      res.append(s)