class Solution(object):
    def searchRange(self, nums, target):
        def search(n, lo, hi):
            while lo < hi:
                mid = (lo + hi) / 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        lo = search(target, 0, len(nums) - 1)
        if nums[lo] != target:
            return [-1, -1]
        return [lo, search(target + 1, lo, len(nums) - 1) - 1]
