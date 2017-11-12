class Solution(object):
  def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    m = {}
    for c in s:
      if c not in m:
        m[c] = 1
      else:
        m[c] += 1
    for i, c in enumerate(s):
      if m[c] == 1:
        return i
    return -1