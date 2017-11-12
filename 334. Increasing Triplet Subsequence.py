class Solution(object):
  def increasingTriplet(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) < 3:
      return False
    i, j = float('inf'), float('inf')
    for num in nums:
      if i < num <= j:
        j = num
      elif num <= i:
        i = num
      else:
        if i < j:
          return True
    return False