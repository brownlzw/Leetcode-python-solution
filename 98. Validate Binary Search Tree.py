# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stk = []
        cur = root
        prev = None
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            if prev and prev.val >= cur.val:
                return False
            prev = cur
            cur = cur.right

        return True

        return self.validateBST(root, float("inf"), -float("inf"))

        def validateBST(self, root, max_num, min_num):
            if not root: return True
            if root.val >= max_num or root.val <= min_num: return False
            return self.validateBST(root.left, root.val, min_num) and self.validateBST(root.right, max_num, root.val)

        # O(n), O(d) ~ O(logn)/O(n)
