from collections import deque
class Solution(object):
  def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    res = []
    dq = deque()
    l = len(nums)
    for i, num in enumerate(nums):
      if i >= k and dq[0] <= i - k:
        dq.popleft()
      while dq and nums[dq[-1]] < num:
        dq.pop()
      dq.append(i)
      if i >= k - 1:
        res.append(nums[dq[0]])
    return res

