# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
         # Return None immediately if either list is empty
        if not headA or not headB:
            return None
            
        pA = headA
        pB = headB
        
        # Loop continues until pA and pB point to the same node (or both are None)
        while pA != pB:
            # Switch to headB if end of listA is reached, else move forward
            pA = headB if pA is None else pA.next
            
            # Switch to headA if end of listB is reached, else move forward
            pB = headA if pB is None else pB.next
            
        # Returns either the intersecting node reference or None
        return pA
