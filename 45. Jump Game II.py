class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = count = bound = 0
        for i in range(len(nums) - 1):
            right = max(i + nums[i], right)
            if i == bound:
                count += 1
                bound = right
        return count