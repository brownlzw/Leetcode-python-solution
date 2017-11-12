class Solution(object):
  def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    if len(p) > len(s):
      return []
    m = {}
    count = 0
    res = []
    for c in p:
      if c not in m:
        count += 1
        m[c] = 1
      else:
        m[c] += 1
    lp =len(p)
    for i in xrange(lp):
      if s[i] in m:
        m[s[i]] -= 1
        if not m[s[i]]:
          count -= 1
    if not count:
      res.append(lp - 1)
    for i in xrange(lp, len(s)):
      if s[i - lp] in m:
        m[s[i - lp]] += 1
        if m[s[i - lp]] == 1:
          count += 1
      if s[i] in m:
        m[s[i]] -= 1
        if not m[s[i]]:
          count -= 1
      if not count:
        res.append(i)
    return res