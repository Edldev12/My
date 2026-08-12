# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Pointer to write the modified summed blocks
        modify = head.next
        # Pointer to traverse and calculate block sums
        traverse = head.next
        
        while traverse:
            total_sum = 0
            # Sum up all non-zero nodes until the next zero marker
            while traverse and traverse.val != 0:
                total_sum += traverse.val
                traverse = traverse.next
            
            # Overwrite the modify pointer's value with the computed sum
            modify.val = total_sum
            # Advance traverse past the current zero node
            traverse = traverse.next
            # Link the modified node to the next section's starting point
            modify.next = traverse
            # Move modify forward for the next sum block
            modify = modify.next
            
        return head.next
