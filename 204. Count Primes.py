class Solution(object):
  def countPrimes(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 2:
      return 0
    array = [False] * n
    count = 1
    nsqrt = int(n ** 0.5) + 1
    for base in xrange(3, n, 2):
      if not array[base]:
        count += 1
        array[base ** 2:: 2 * base] = [True] * len(range(base ** 2, n, 2 * base))
    return count

