class Solution(object):
  def myAtoi(self, str):
    """
    :type str: str
    :rtype: int
    """
    str = str.strip()
    if not str:
      return 0
    if str[0] == '-':
      sign = -1
      str = str[1:]
    elif str[0] == '+':
      sign = 1
      str = str[1:]
    elif str[0].isdigit():
      sign = 1
    else:
      return 0

    if not str:
      return 0
    num = 0
    for c in str:
      if c.isdigit():
        if sign == 1 and (num > 214748364 or 2147483647 - int(c) < num * 10):
          return 2147483647
        elif sign == -1 and (-num < -214748364 or -2147483648 + int(c) > -10 * num):
          return -2147483648

        num = num * 10 + int(c)
      else:
        return sign * num
    return sign * num
