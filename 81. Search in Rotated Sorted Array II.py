class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) / 2

            if nums[mid] == target:
                return True
            # if all three are equals, we can't tell pivot is in which part
            if nums[hi] == nums[lo] == nums[mid]:
                hi -= 1
                lo += 1
                # pivot is in the right part:
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # pivot is in the left part:
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False