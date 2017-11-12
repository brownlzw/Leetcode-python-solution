class Solution(object):
  def maxRotateFunction(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    l = len(A)
    total = res = 0
    for i, num in enumerate(A):
      res += i * num
      total += num
    cur = res
    for i in xrange(l - 1, 0, -1):
      cur += total - l * A[i]
      if cur > res:
        res = cur
    return res