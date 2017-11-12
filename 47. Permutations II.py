class Solution(object):
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n: break  # handles duplication
            ans = new_ans
        return ans
    # To handle duplication, just avoid inserting a number before any of its duplicates.
    # O(n * (n-1)! * l), O(n!)