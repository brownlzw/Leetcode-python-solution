class Solution(object):
  def findTargetSumWays(self, nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    if not nums:
      return 0
    sums = sum(nums)
    if S > sums or S < -sums or (sums + S) % 2 != 0:
      return 0
    target = (sums + S) / 2
    dp = [0] * (target + 1)
    dp[0] = 1
    cur_sum = 0
    for num in nums:
      cur_sum += num
      for i in xrange(min(cur_sum, target), num - 1, -1):
        dp[i] += dp[i - num]
    return dp[target]

