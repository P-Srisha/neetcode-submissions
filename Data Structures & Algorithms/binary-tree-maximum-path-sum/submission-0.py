# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxVal = float("-inf")

        def sumPath(curr):
            if not curr:
                return 0
            
            left = max(0, sumPath(curr.left))
            right = max(0, sumPath(curr.right))

            self.maxVal = max(self.maxVal, curr.val + left + right)

            return curr.val + max(left, right)
        
        sumPath(root)
        return self.maxVal