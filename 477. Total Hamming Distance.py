class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            mask = 1 << i
            zeros, ones = 0, 0
            for num in nums:
                if not (num & mask):
                    ones += 1
                else:
                    zeros += 1
                res += ones * zeros
        return res
    # O(32n), O(1)