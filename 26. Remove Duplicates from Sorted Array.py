class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        j = 0
        for i in xrange(1, l):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1
