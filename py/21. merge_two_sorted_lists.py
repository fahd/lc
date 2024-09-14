# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2
    
        node = ListNode(-1, None)

        l1ref = list1
        l2ref = list2

        noderef = node

        while l1ref and l2ref:
            l1rv = l1ref.val
            l2rv = l2ref.val
            

            if l1rv <= l2rv:
                noderef.next = l1ref
                l1ref = l1ref.next
            elif l2rv < l1rv:
                noderef.next = l2ref
                l2ref = l2ref.next
            
            noderef = noderef.next
        
        if not l1ref and l2ref:
            noderef.next = l2ref
        if not l2ref and l1ref:
            noderef.next = l1ref
        
        return node.next

        