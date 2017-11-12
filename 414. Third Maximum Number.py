class Solution(object):
  def thirdMax(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    m1 = m2 = m3 = -float('inf')
    for num in nums:
      if num == m1 or num == m2 or num == m3:
        continue
      if num > m1:
        m1, m2, m3 = num, m1, m2
      elif num > m2:
        m2, m3 = num, m2
      elif num > m3:
        m3 = num
    return m1 if m3 == -float('inf') else m3