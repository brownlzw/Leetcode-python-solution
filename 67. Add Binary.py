class Solution(object):
  def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if len(a) > len(b):
            b = "0" * (len(a) - len(b) ) + b
    elif len(b) > len(a):
        a = "0" * (len(b) - len(a)) + a

    ans = ""
    carry = 0

    for i in reversed(range(len(a))):
        carry += (a[i] == '1') + (b[i] == '1')
        ans = str(carry & 1) + ans
        carry >>= 1

    if carry > 0:
        ans = str(carry) + ans
    return ans