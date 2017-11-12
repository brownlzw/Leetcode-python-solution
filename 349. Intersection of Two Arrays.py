class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not len(nums1) or not len(nums2):
            return []
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
        s = set()
        for num in nums1:
            if num not in s:
               s.add(num)
        res = []
        for num in nums2:
            if num in s:
                res.append(num)
                s.discard(num)
        return res
    # O(m + n), O(min(m, n))