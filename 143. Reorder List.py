# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = prev = None
        while head2:
            head2.next, head2, prev = prev, head2.next, head2
        tail = prev
        while tail:
            head.next, tail.next, head, tail = tail, head.next, head.next, tail.next
    # O(n), O(1)