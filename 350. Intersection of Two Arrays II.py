from bisect import bisect_right
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = {}
        for c in nums1:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
        res = []
        for c in nums2:
            if c in m:
                res.append(c)
                m[c] -= 1
                if not m[c]:
                    m.pop(c)
        return res

    def inter2(self, nums1, nums2):
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                while i < len(nums1) and nums1[i] == nums1[i - 1]:
                    i += 1
                while j < len(nums2) and nums2[j] == nums2[j - 1]:
                    j += 1
        return res
    # O(m + n)

    def inter3(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        i = 0
        res = []
        for num in nums1:
            i = bisect_right(nums2, num, i)
            if i and nums2[i - 1] == num:
                res.append(num)
            if i == len(nums2):
                break