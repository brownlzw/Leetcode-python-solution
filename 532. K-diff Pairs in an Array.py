class Solution(object):
  def findPairs(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if k < 0:
      return 0
    m = set()
    visit = set()
    res = 0
    for num in nums:
      if num - k in m and num - k not in visit:
        res += 1
        visit.add(num - k)
      if num + k in m and num not in visit:
        res += 1
        visit.add(num)
      m.add(num)
    return res
