# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(curr):
            if not curr:
                res.append("null")
                return
            
            res.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")

        i = 0

        def buildTree():
            nonlocal i
            if nodes[i] == "null":
                i += 1
                return None

            curr = TreeNode(int(nodes[i]))
            i += 1
            curr.left = buildTree()
            curr.right = buildTree()

            return curr

        root = buildTree()
        return root