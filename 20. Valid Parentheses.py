class Solution(object):
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    m = {'(':')', "[":']', '{':'}'}
    s = []
    for c in s:
      if c in s:
        s.append(c)
      else:
        if not s or m[s[-1]] != c:
          return False
        s.pop()
    return not s