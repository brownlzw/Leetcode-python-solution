# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        cur = head
        while cur:
            copy = RandomListNode(cur.label)
            cur.next, copy.next = copy, cur.next
            cur = copy.next
        cur = head
        while cur:
            copy = cur.next
            copy.random = cur.random.next if cur.random else None
            cur = copy.next
        cur = head
        dummy = RandomListNode(0)
        cur_copy = dummy
        while cur:
            cur.next, cur_copy.next = cur.next.next, cur.next
            cur = cur.next
            cur_copy = cur_copy.next
        return dummy.next
    # O(n), O(n)
