# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def traverse(head: Optional[ListNode]) -> bool:
    t = head
    h = head
    
    # empty or single node
    if not head or not head.next:
        return False

    while t or h:
        if h and t and h.next == t:
            return True
        if t:
            t = t.next
        if h:
            h = h.next
            if h:
                h = h.next
    return False
    
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return traverse(head)
