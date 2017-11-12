class Solution(object):
  def minSubArrayLen(self, s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    i, j, sum = 0, 0, 0
    min_len = len(nums) + 1
    while j < len(nums):
      while j < len(nums) and sum < s:
        sum += nums[j]
        j += 1
      while sum >= s:
        min_len = min(min_len, j - i)
        sum -= nums[i]
        i += 1
    return 0 if min_len == (len(nums) + 1) else min_len
