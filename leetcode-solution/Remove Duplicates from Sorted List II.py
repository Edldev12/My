# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # Step 2: Initialize 'prev' pointer at the dummy node
        prev = dummy
        
        while head:
            # Step 3: Check if the current node has a duplicate ahead
            if head.next and head.val == head.next.val:
                # Skip all nodes with this duplicate value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Relink 'prev' to the node after all duplicates
                prev.next = head.next
            else:
                # No duplicates found, move 'prev' forward
                prev = prev.next
                
            # Move 'head' forward to continue the traversal
            head = head.next
            
        return dummy.next
