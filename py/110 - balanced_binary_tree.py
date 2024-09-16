# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def travel(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    lh = travel(root.left)
    rh = travel(root.right)

    if lh == -1 or rh == -1:
        return -1
    
    elif abs(lh - rh) > 1:
        return -1

    return 1 + max(lh,rh)
    
    

    # if math.max(rh - lh) > 1:
    #     return False
    

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return travel(root) > -1
        
        
        
        