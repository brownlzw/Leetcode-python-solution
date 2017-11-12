class Solution(object):
  def findErrorNums(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    m = set()
    n = len(nums)
    twice, miss = 0, 0
    for num in nums:
      if num in m:
        twice = num
      else:
        m.add(num)
    for i in range(1, n + 1):
      if i not in m:
        miss = i
        break
    return [twice, miss]

    rightSum = (1 + len(nums)) * len(nums) / 2
    noRepeatSum = sum(set(nums))
    currentSum = sum(nums)
    return [currentSum - noRepeatSum, rightSum - noRepeatSum]