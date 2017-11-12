class Solution(object):
  def isOneEditDistance(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if s == t:
        return False
    l1, l2 = len(s), len(t)
    if l1 > l2:
        return self.isOneEditDistance(t, s)
    if l2 - l1 > 1:
        return False
    for i in xrange(len(s)):
        if s[i] != t[i]:
            if l1 == l2:
                s = s[:i] + t[i] + s[i+1:]
            else:
                s = s[:i] + t[i] + s[i:]

            break
    return s == t or s == t[:-1]