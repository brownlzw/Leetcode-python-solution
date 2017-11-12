from random import randint
class Solution(object):
  def __init__(self, nums):
    """

    :type nums: List[int]
    :type numsSize: int
    """
    self.nums = nums

  def pick(self, target):
    """
    :type target: int
    :rtype: int
    """
    count = 0
    res = None
    for i, num in enumerate(self.nums):
      if num == target:
        if not randint(0, count):
          res = i
        count += 1
    return res




    # Your Solution object will be instantiated and called as such:
    # obj = Solution(nums)
    # param_1 = obj.pick(target)