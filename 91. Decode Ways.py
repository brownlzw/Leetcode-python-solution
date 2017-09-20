class Solution(object):
  def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s or s[0] == '0':
        return 0
    n = len(s)
    x1, x2, cur = 1, 1, 1
    for i in range(1, n):
      if s[i] == '0':
        if s[i-1] in "12":
          cur = x1
        else:
          return 0
      else:
        cur = x2
        if s[i - 1] == "1" or (s[i - 1] == "2" and s[i] in "123456"):
          cur += x1
      x1 = x2
      x2 = cur
    return cur
