class Solution(object):
  def findWords(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    result = []
    r1 = str('qwertyuiopQWERTYUIOP')
    r2 = str('asdfghjklASDFGHJKL')
    r3 = str('zxcvbnmZXCVBNM')
    for item in words:
      if all((letter in r1) for letter in item):
        result.append(item)
      elif all((letter in r2) for letter in item):
        result.append(item)
      elif all((letter in r3) for letter in item):
        result.append(item)
    return result