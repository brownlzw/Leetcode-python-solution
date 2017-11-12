class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums) - 1
        while i < j and nums[i] == 0:
            i += 1
        while i < j and nums[j] == 2:
            j -= 1
        k = i
        while k <= j:
            if not nums[k]:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1
            elif nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
    # O(n), O(1)