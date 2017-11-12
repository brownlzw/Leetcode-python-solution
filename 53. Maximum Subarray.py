class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = nums[0]
        sums = 0
        for i in nums:
            if sums < 0:
                sums = i
            else:
                sums += i
            if sums > maxs:
                maxs = sums
        return maxs
    # O(n), O(1)