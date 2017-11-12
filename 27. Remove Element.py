class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j