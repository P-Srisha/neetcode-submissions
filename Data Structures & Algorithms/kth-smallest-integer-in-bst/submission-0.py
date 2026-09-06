# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        res = []
        def inorder(curr):
            if not curr:
                return None
            inorder(curr.left)
            res.append(curr.val)
            inorder(curr.right)

        inorder(root)

        return res[k - 1]