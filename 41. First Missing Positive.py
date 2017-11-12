class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        n = len(nums)
        m = max(nums)
        if m <= 0:
            return 1
        for i, num in enumerate(nums):
            if num <= 0 or num >= len(nums):
                nums[i] = m
        for num in nums:
            idx = abs(num) - 1
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] = -nums[idx]
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return len(nums) + 1
