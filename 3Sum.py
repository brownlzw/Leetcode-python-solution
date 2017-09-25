class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
      if i > 0 and nums[i] == nums[i-1]:
        continue
      if nums[i] + nums[i + 1] + nums[i + 2] > 0:
        break
      self.twosum(res, nums, i + 1, -nums[i])
    return res

    # if not nums or len(nums) < 3:
    #   return []
    #
    # counter = {}
    # for n in nums:
    #   counter[n] = counter.get(n, 0) + 1
    #
    # uniq = counter.keys()
    # pos = sorted([x for x in uniq if x >= 0])
    # neg = sorted([x for x in uniq if x < 0])
    #
    # ret = []
    # # 3
    # if counter.get(0, 0) >= 3:
    #   ret.append([0, 0, 0])
    #
    # for p in pos:
    #   for n in neg:
    #     r = -(p + n)
    #     if r in counter:
    #       if (r == p or r == n) and counter[r] > 1:
    #         ret.append([n, r, p])
    #       elif r < n:
    #         ret.append([r, n, p])
    #       elif r > p:
    #         ret.append([n, p, r])
    #
    # return ret

  def twosum(self, res, nums, low, target):
    if nums[low] + nums[low + 1] > target or nums[-2] + nums[-1] < target:
      return
    low, high = low, len(nums)-1
    while low < high:
      val = nums[low] + nums[high]
      if val == target:
        res.append([-target, nums[low], nums[high]])
        low += 1
        while low < high and nums[low] == nums[low - 1]:
          low += 1
        high -= 1
        while low < high and nums[high] == nums[high + 1]:
          high -= 1
      elif val > target:
        high -= 1
      else:
        low += 1
