# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse(root: Optional[TreeNode], o) -> int:
    if not root:
        return 0
    
    lh = traverse(root.left, o)
    rh = traverse(root.right, o)

    o["md"] = max(o["md"], lh + rh)

    return 1 + max(lh,rh)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        o = {"md": 0}
        traverse(root, o)
        return o["md"]

        