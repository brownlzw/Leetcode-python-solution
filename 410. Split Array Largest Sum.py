class Solution(object):
  def splitArray(self, nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """

    def valid(mid):
      cnt = 0
      current = 0
      for n in nums:
        current += n
        if current > mid:
          cnt += 1
          if cnt >= m:
            return False
          current = n
      return True

    l = max(nums)
    h = sum(nums)

    while l < h:
      mid = l + (h - l) / 2
      if valid(mid):
        h = mid
      else:
        l = mid + 1
    return l