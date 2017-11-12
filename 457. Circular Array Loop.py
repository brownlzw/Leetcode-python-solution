class Solution(object):
  def circularArrayLoop(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    for i in xrange(n):
      if nums[i] > 0 and nums[i] != n:
        start = i
        count = 0
        while nums[start] > 0:
          count += nums[start]
          if count % n == 0:
            return True
          nums[start], start = 0, (start + nums[start]) % n,

    for i in xrange(n - 1, -1, -1):
      if nums[i] < 0and nums[i] != -n:
        end = i
        count = 0
        while nums[end] < 0:
          count -= nums[end]
          if count % n == 0:
            return True
          nums[end], end = 0, (end + nums[end]) % n
    return False

# slow,fast
    def jump(i):
      n = len(nums)
      return (i + nums[i]) % n

    for i in range(len(nums)):
      if nums[i] == 0:
        continue
      tortoise = i
      hare = jump(i)
      while tortoise != hare and nums[i] * nums[hare] > 0 and nums[i] * nums[jump(hare)] > 0:
        tortoise = jump(tortoise)
        hare = jump(hare)
        hare = jump(hare)
      if tortoise == hare and hare != jump(hare):
        return True
      hare = i
      while nums[jump(hare)] * nums[i] > 0:
        temp = jump(hare)
        nums[hare] = 0
        hare = temp
    return False

