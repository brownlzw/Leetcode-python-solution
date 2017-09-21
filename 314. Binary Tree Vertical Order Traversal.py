# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
  def verticalOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    if not root:
      return res
    left = 0
    dict = {root: 0}
    queue = collections.deque([root])
    while len(queue):
      cur = queue.popleft()
      index = dict[cur]
      if index < left:
        res.insert(0, [cur.val])
        left -= 1
      elif index - left >= len(res):
        res.append([cur.val])
      else:
        res[index - left].append(cur.val)
      if cur.left:
        dict[cur.left] = index - 1
        queue.append(cur.left)
      if cur.right:
        dict[cur.right] = index + 1
        queue.append(cur.right)
    return res

    # using deque and defaultlist
    # cols = collections.defaultdict(list)
    # queue = collections.deque([(root, 0)])
    # while queue:
    #   node, i = queue.popleft()
    #   if node:
    #     cols[i].append(node.val)
    #     queue += (node.left, i - 1), (node.right, i + 1)
    # return [cols[i] for i in sorted(cols)]

