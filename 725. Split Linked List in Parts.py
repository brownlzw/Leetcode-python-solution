# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res = []
        l = 0
        cur = root
        while cur:
            cur = cur.next
            l += 1
        n, mod = l / k, l % k
        prev, cur = None, root
        for _ in xrange(k):
            res.append(cur)
            if mod and cur:
                prev, cur = cur, cur.next
                mod -= 1
            for _ in xrange(n):
                if not cur:
                    break
                prev, cur = cur, cur.next
            if prev:
                prev.next = None
        return res