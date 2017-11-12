class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        m = {0: 1}
        tot = cnt = 0
        for num in nums:
            tot += num
            if tot - k in m:
                cnt += m[tot - k]
            if tot not in m:
                m[tot] = 1
            else:
                m[tot] += 1
        return cnt
    # O(n), O(n)