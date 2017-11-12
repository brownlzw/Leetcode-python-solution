class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            # nums[l] <= nums[mid] means on the same part, so l = mid + 1 if
            elif nums[l] <= nums[mid] < target or target < nums[l] <= nums[mid] or nums[mid] < target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1

