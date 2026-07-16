# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
         # Initialize both pointers to the head
        slow = head
        fast = head
        
        # Traverse until fast reaches the end of the list
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
            # If they meet, a cycle exists
            if slow == fast:
                return True
                
        # Fast reached the end, so no cycle exists
        return False
