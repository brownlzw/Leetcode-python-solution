class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def helper(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if not nums or not k:
            return
        n = len(nums)
        k %= n
        # nums[:k], nums[k:] = nums[-k:], nums[:-k]
        helper(0, n - k - 1)
        helper(n - k, n - 1)
        helper(0, n - 1)
    # O(n), O(1)
