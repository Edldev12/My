# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Track the node right before the current group starts
        prev_group_end = head
        curr = head.next
        
        # We start looking for group 2 (group 1 has size 1, always odd, never reversed)
        expected_len = 2
        
        while curr:
            # Step 1: Count how many nodes actually exist in the current group
            actual_len = 0
            count_ptr = curr
            while count_ptr and actual_len < expected_len:
                actual_len += 1
                count_ptr = count_ptr.next
                
            # Step 2: If the actual length is even, reverse this segment
            if actual_len % 2 == 0:
                # Standard in-place linked list reversal for 'actual_len' nodes
                rev_prev = None
                rev_curr = curr
                for _ in range(actual_len):
                    nxt = rev_curr.next
                    rev_curr.next = rev_prev
                    rev_prev = rev_curr
                    rev_curr = nxt
                
                # Reconnect the reversed group back into the main list
                # prev_group_end should now point to the new head of this group (rev_prev)
                # The original head of this group (curr) is now the tail, pointing to rev_curr
                tail = curr
                prev_group_end.next = rev_prev
                tail.next = rev_curr
                
                # Move prev_group_end to the tail of our newly reversed group
                prev_group_end = tail
                curr = rev_curr
            else:
                # Step 3: If odd, skip reversal. Just move pointers to the end of this group
                for _ in range(actual_len):
                    prev_group_end = curr
                    curr = curr.next
            
            # Increment expected length for the next group
            expected_len += 1
            
        return head
