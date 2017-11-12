class Solution(object):
  def findLengthOfLCIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0
    n = len(nums)
    prev = 1
    res = 0
    for i in range(1, len(nums)):
      cur = 0
      if nums[i] > nums[i - 1]:
        cur = prev + 1
      if cur > res:
        res = cur
      prev = cur
    return res