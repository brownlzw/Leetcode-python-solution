def moveZeroes(self, nums):
  """
  :type nums: List[int]
  :rtype: void Do not return anything, modify nums in-place instead.
  """
  i = 0
  for num in nums:
    if num:
      nums[i] = num
      i += 1
  for j in range(i, len(nums)):
    nums[j] = 0