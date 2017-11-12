# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def dfs(root, tmp, res):
            if not root:
                return
            tmp.append(str(root.val))
            if not root.left and not root.right:
                res.append("->".join(tmp))
                tmp.pop()
                return
            dfs(root.left, tmp, res)
            dfs(root.right, tmp, res)
            tmp.pop()

        tmp = []
        res = []
        if not root:
            return res
        dfs(root, tmp, res)
        return res
    # O(n), O(nlogn)