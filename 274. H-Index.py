class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        count = [0] * (l + 1)
        for num in citations:
            if num > l:
                count[l] += 1
            else:
                count[num] += 1
        total = 0
        for i in xrange(l, -1, -1):
            total += count[i]
            if total >= i:
                return i
        return 0

    # O(n), O(n)
