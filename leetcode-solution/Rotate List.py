# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) ->Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
            
        # 1. Compute the length of the list and find the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # 2. Handle cases where k >= length
        k = k % length
        if k == 0:
            return head  # No rotation needed
            
        # 3. Connect tail to head to form a circular loop
        tail.next = head
        
        # 4. Find the new tail position: (length - k) steps from the head
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        # 5. Break the ring and establish the new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
