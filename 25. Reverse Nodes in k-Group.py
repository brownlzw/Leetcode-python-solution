# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def reverseKGroup(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    while True:
      count = 0
      while r and count < k:
        r = r.next
        count += 1
      if count == k:
        prev, cur = r, l
        for _ in xrange(k):
          cur.next, prev, cur = prev, cur, cur.next
        jump.next, jump, l = prev, l, r
      else:
        return dummy.next
