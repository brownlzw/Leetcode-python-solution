class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l ,r = 0 ,len(height) - 1
        max_area = 0
        while l < r:
            if height[l] < height[r]:
                cur = height[l] * (r - l)
                l += 1
            else:
                cur = height[r] * (r - l)
                r -= 1
            if cur > max_area:
                max_area = cur
        return max_area
