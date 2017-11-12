class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l, r = 0, len(height) - 1
        maxl, maxr = 0, 0
        while l <= r:
            if maxl < maxr:
                if height[l] < maxl:
                    res += maxl - height[l]
                else:
                    maxl = height[l]
                l += 1
            else:
                if height[r] < maxr:
                    res += maxr - height[r]
                else:
                    maxr = height[r]
                r -= 1
        return res
