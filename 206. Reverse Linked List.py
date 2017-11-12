# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        tmp = head.next
        tail = self.reverseList(tmp)
        head.next = None
        tmp.next = head
        return tail

        prev = None
        cur = head
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        return prev
    # O(n), O(1)