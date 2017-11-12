class Solution(object):
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start, end = {}, {}
    longest = 0
    for num in nums:
      s, e = num, num
      if num in start or num in end:
        continue
      if num + 1 in start:
        e = start[num + 1]
        del start[num + 1]
      if num - 1 in end:
        s = end[num - 1]
        del end[num - 1]
      longest = max(longest, e - s + 1)
      start[s] = e
      end[e] = s
    return longest

    nums = set(nums)
    best = 0
    for x in nums:
      if x - 1 not in nums:
        y = x + 1
        while y in nums:
          y += 1
        best = max(best, y - x)
    return best

