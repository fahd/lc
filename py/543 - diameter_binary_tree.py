# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def __init__(self):
        self.max_diameter = 0

    def traverse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        lh = self.traverse(root.left)
        rh = self.traverse(root.right)

        self.max_diameter = max(self.max_diameter, lh + rh)

        return 1 + max(lh,rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.max_diameter

        