# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Dummy node points to the start of the sorted list
        dummy = ListNode(0)
        dummy.next = head
        
        # prev marks the end of the sorted part, curr is the unsorted node
        prev = head
        curr = head.next
        
        while curr:
            # Optimization: If it's already larger than the largest sorted element,
            # just advance the sorted boundary.
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
            else:
                # Store the next node to process later
                next_node = curr.next
                
                # Start searching from the dummy node for the insertion position
                p = dummy
                while p.next.val < curr.val:
                    p = p.next
                
                # Insert curr between p and p.next
                prev.next = next_node  # Remove curr from its old position
                curr.next = p.next     # Point curr to the rest of the list
                p.next = curr          # Link p to curr
                
                # Move to the next unsorted node
                curr = next_node
                
        return dummy.next
