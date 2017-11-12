class Solution(object):
  def validPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    length = len(s)
    res = s[::-1]
    if s == res:
      return True
    for i in xrange(length):
      if s[i] != s[~i]:
        return s[i + 1: length -i] == res[i:~i] or s[i:~i] == res[i + 1: length - i]
    return True
