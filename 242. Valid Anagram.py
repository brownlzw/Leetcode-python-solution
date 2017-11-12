class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
      return False
    m = {}
    for c in s:
      if c not in m:
        m[c] = 1
      else:
        m[c] += 1
    for c in t:
      if c not in m:
        return False
      m[c] -= 1
      if not m[c]:
        del m[c]
    return not m