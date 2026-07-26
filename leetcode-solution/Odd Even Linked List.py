# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head          # Tracks the last node in the odd list
        even = head.next    # Tracks the last node in the even list
        even_head = even    # Saves the start of the even list to connect later
        
        # Loop until there are no more even nodes or next odd nodes
        while even and even.next:
            odd.next = even.next  # Connect current odd to the next odd node
            odd = odd.next        # Move odd pointer forward
            
            even.next = odd.next  # Connect current even to the next even node
            even = even.next      # Move even pointer forward
            
        # Connect the end of the odd list to the head of the even list
        odd.next = even_head
        
        return head
