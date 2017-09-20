class Solution(object):
  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
  #   if len(digits) == 0:
  #     return []
  #   numbers = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
  #   current = []
  #   result = []
  #   self.helper(current, result, digits, 0, numbers)
  #   return result
  #
  # def helper(self, current, result, digits, index, numbers):
  #   if index == len(digits):
  #     result.append(''.join(current))
  #     return
  #
  #   chars = numbers[int(digits[index])]
  #   for char in chars:
  #     current.append(char)
  #     if index < len(digits):
  #       self.helper(current, result, digits, index + 1, numbers)
  #     current.pop()
    if '' == digits: return []
    kvmaps = {
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz'
    }
    return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])  # reduce