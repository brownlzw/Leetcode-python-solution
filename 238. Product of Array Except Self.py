class Solution(object):
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
      return []
    res = [1] * len(nums)
    prod = nums[0]
    for i in xrange(1, len(nums)):
      res[i] = prod
      prod *= nums[i]
    prod = nums[-1]
    for i in xrange(len(nums) - 2, -1, -1):
      res[i] *= prod
      prod *= nums[i]
    return res
