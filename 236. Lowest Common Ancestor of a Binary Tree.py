# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

        # find the length of shortest path between two nodes in a tree
        if not root: return None

        d = {root: (None, 0)}
        dq = collections.deque()
        dq.append(root)
        while dq:
            curr = dq.popleft()
            h = d[curr][1]
            if curr.left:
                d[curr.left] = (curr, h + 1)
                dq.append(curr.left)

                if curr.right:
                    d[curr.right] = (curr, h + 1)
                dq.append(curr.right)
        d2 = {p}
        p1 = p
        while d[p][0]:
            d2.add(d[p][0])
            p = d[p][0]
        # print(d2)
        q1 = q
        while q:
            if q in d2:
                return d[p1][1] + d[q1][1] - d[q][1] * 2
            q = d[q][0]

        return d[p1][1] + d[q1][1]
