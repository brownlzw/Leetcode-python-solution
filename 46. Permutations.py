class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(pos):
            if pos == len(nums):
                res.append(nums[:])
            for i in xrange(pos, len(nums)):
                nums[pos], nums[i] = nums[i], nums[pos]
                dfs(pos + 1)
                nums[pos], nums[i] = nums[i], nums[pos]

        res = []
        dfs(0)
        return res

        res = [[]]
        for n in nums:
            new_perms = []
            for perm in res:
                new_perms += [perm[:i] + [n] + perm[i:] for i in range(len(perm) + 1)]
            res = new_perms
        return res
    # O(n!), O(n!)
