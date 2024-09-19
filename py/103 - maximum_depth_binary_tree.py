# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse(node:Optional[TreeNode]) -> int:
    if not node:
        return 0
    lh = traverse(node.left)
    rh = traverse(node.right)

    return 1 + max(lh, rh)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return traverse(root)