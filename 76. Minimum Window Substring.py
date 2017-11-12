class Solution(object):
  def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not s or len(t) > len(s):
      return ""
    m = {}
    count = 0
    for char in t:
      if char not in m:
        m[char] = 1
        count += 1
      else:
        m[char] += 1
    i = 0
    min_i, min_j, min_len = -1, -1, len(s) + 1
    for j in xrange(len(s)):
      cur = s[j]
      if cur in m:
        m[cur] -= 1
        if not m[cur]:
          count -= 1
        while not count:
          left = s[i]
          if left in m:
            m[left] += 1
            if m[left] > 0:
              count += 1
            if count > 0 and j - i + 1 < min_len:
              min_i = i
              min_j = j
              min_len = j - i + 1
          i += 1
    return "" if min_i == -1 else s[min_i : min_j + 1]


