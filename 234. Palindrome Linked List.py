# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    prev = None
    fast = head
    while fast and fast.next:
      fast = fast.next.next
      head.next, prev, head = prev, head, head.next
    tail = head.next if fast else head
    isPali = True
    while prev:
      isPali = isPali and prev.val == tail.val
      prev.next, head, prev = head, prev, prev.next
      tail = tail.next
    return isPali