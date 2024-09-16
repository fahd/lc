# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lca(root:'TreeNode', p:'TreeNode', q:'TreeNode'):
    if root == None:
        return
    l = p if p.val < q.val else q
    r = p if p.val > q.val else q

    if l.val < root.val and r.val > root.val:
        return root
    
    elif l.val <= root.val and r.val > root.val:
        return l
    elif r.val >= root.val and l.val < root.val:
        return r
    elif l.val < root.val and r.val < root.val:
        return lca(root.left, p, q)
    elif l.val > root.val and r.val > root.val:
        return lca(root.right, p, q)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = lca(root, p, q)
        return node


        