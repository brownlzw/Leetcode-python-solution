class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        right = 0
        for i in xrange(len(nums)):
            if i > right:
                return False
            if i + nums[i] > right:
                right = i + nums[i]
            if right >= len(nums) - 1:
                return True