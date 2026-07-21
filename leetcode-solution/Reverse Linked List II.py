# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Use a dummy node to seamlessly handle changes at the head node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 1: March 'prev' to the node right before position 'left'
        for _ in range(left - 1):
            prev = prev.next
            
        # Step 2: Set markers for the sublist boundary
        curr = prev.next  # This will become the tail of the reversed sublist
        
        # Step 3: Continuously cut out 'nxt' and insert it right after 'prev'
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
            
        return dummy.next
