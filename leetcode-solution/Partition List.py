# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        # Step 2: Initialize pointers to track the tail of each partition
        less = less_dummy
        greater = greater_dummy
        
        # Step 3: Traverse the original linked list
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
            
        # Step 4: Prevent cycles by terminating the greater list
        greater.next = None
        
        # Step 5: Stitch the two partitions together
        less.next = greater_dummy.next
        
        return less_dummy.next
