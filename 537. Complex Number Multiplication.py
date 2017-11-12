class Solution(object):
  def complexNumberMultiply(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    m = n = p = q = 0
    j = a.find('+', 1)
    m, n = int(a[0:j]), int(a[j + 1:-1])
    j = b.find('+', 1)
    p, q = int(b[0:j]), int(b[j + 1:-1])
    re, im = m * p - n * q, m * q + n * p
    return str(re) + '+' + str(im) + 'i'