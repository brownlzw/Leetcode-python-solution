class Solution(object):
  def maxSubArrayLen(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    d = {0: -1}
    sum = 0
    res = 0
    for i, num in enumerate(nums):
      sum += num
      if sum - k in d:
        res = max(res, i - d[sum - k])
      if sum not in d:
        d[sum] = i
    return res