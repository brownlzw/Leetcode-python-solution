class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
      return len(nums)
    index = 2
    for i in range(2, len(nums)):
      if nums[i] != nums[index - 2]:
        nums[index] = nums[i]
        index += 1
    return index
