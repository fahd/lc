# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        o = []

        o = o + self.inorderTraversal(root.left)
        o = o + [root.val]
        o = o + self.inorderTraversal(root.right)
        return o