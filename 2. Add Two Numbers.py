# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    dummy = ListNode(0)
    cur = dummy
    while l1 or l2:
      if l1:
        carry += l1.val
        l1 = l1.next
      if l2:
        carry += l2.val
        l2 = l2.next
      cur.next = ListNode(carry%10)
      carry /= 10
      cur = cur.next
    if carry:
      cur.next = ListNode(carry)
    return dummy.next
