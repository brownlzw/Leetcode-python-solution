class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        l = 0
        r = min(citations[-1], len(citations))
        best_h = 0
        while l <= r:
            h = (l + r) / 2
            if citations[-h] >= h:
                best_h = h
                l = h + 1
            else:
                r = h - 1

        return best_h
    # O(logr)

