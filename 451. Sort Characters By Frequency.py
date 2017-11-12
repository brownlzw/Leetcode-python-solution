class Solution(object):
  def frequencySort(self, s):
    """
    :type s: str
    :rtype: str
    """
    m = {}
    for c in s:
      if c not in m:
        m[c] = 1
      else:
        m[c] += 1
    li = sorted([(m[i], i) for i in m], reverse=True)
    res = []
    for count, c in li:
      res.append(c * count)
    return ''.join(res)
