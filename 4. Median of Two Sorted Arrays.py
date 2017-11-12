class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        l, r = 0, m
        while l <= r:
            i = l + (r - l) / 2
            j = (m + n + 1) / 2 - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                r = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                l = i + 1
            else:
                if not i:
                    max_left = nums2[j - 1]
                elif not j:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])
                if ((m + n) & 1) == 1:
                    return max_left
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                return (max_left + min_right) / 2.0

        l = len(nums1) + len(nums2)
        return self.find_k(nums1, nums2, l // 2) if l % 2 == 1 else (self.find_k(nums1, nums2, l // 2) + \
                                                                    self.find_k(nums1, nums2, l // 2 - 1)) / 2.0

    def find_k(self, a, b, k):
        if len(a) > len(b):
            a, b = b, a
        if not a:
            return b[k]
        if k == len(a) + len(b) - 1:
            return max(a[-1], b[-1])
        i = len(a) // 2
        j = k - i
        if a[i] > j[k]:
            return self.find_k(a[:i], b[j:], i)
        else:
            return self.find_k(a[i:], b[:j], j)