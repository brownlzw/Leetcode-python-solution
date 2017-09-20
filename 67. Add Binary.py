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
        sum_digit = ( int(a[i]) + int(b[i]) + carry )
        carry = sum_digit >> 1
        ans = str(sum_digit & 1) + ans

    if carry > 0:
        ans = str(carry) + ans
    return ans