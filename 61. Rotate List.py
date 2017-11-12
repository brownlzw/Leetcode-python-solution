class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k or not head.next:
            return head
        l = 0
        length = head
        while length:
            l += 1
            length = length.next
        k = k % l
        if not k:
            return head
        slow = fast = head
        for num in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head