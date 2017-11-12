# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq
class Solution(object):
  def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    q = []
    dummy = ListNode(0)
    cur = dummy
    for node in lists:
      if node:
        heapq.heappush(q, (node.val, node))
    while len(q):
      val, node = heapq.heappop(q)
      cur.next = node
      if node.next:
        heapq.heappush(q, (node.next.val, node.next))
      cur = cur.next
    return dummy.next
