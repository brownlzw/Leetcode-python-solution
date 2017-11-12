class Solution(object):
  def findNumberOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0
    n = len(nums)
    dp = [1] * n
    dp2 = [1] * n
    for i in range(1, len(nums)):
      v = 0
      cnt = 1
      for j in xrange(i):
        if nums[i] > nums[j]:
          if dp[j] == v:
            cnt += dp2[j]
          elif dp[j] > v:
            v = dp[j]
            cnt = dp2[j]
      dp[i] = v + 1
      dp2[i] = cnt
    max_v = max(dp)
    res = 0
    for i in xrange(n):
        if dp[i] == max_v:
            res += dp2[i]
    return res
