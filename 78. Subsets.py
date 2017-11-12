class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            new_res = []
            for li in res:
                new_res += [li + [i]]
            res += new_res
        return res

        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res
    # O(2 ^ n), O(2 ^ n)