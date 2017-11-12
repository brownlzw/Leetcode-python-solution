class Solution(object):
  def combinationSum4(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target <= 0:
      return 0
    nums.sort()
    dp = [0] * (target + 1)
    for i in xrange(1, target + 1):
      for num in nums:
        if i < num:
          break
        if i == num:
          dp[i] += 1
        else:
          dp[i] += dp[i - num]
    return dp[-1]