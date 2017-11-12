class Solution(object):
  def checkSubarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if not k:
      return len(nums) > 1 and not any(nums)
    m = {0: -1}
    sum = 0
    k = k if k >= 0 else -k
    for i, num in enumerate(nums):
      sum += num
      if sum % k not in m:
        m[sum % k] = i
      elif m[sum % k] < i - 1:
        return True
    return False
