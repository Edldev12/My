# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # 1. Get total length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        dummy = ListNode(0)
        dummy.next = head
        
        # 2. Bottom-up merge sublists of increasing sizes: 1, 2, 4, 8...
        step = 1
        while step < length:
            prev = dummy
            curr = dummy.next
            
            while curr:
                # Extract the first sublist of size 'step'
                head1 = curr
                head2 = self.split(head1, step)
                
                # Extract the remaining unmerged list
                curr = self.split(head2, step)
                
                # Merge the two sorted sublists and attach to prev
                prev.next = self.merge(head1, head2)
                
                # Move prev to the end of the newly merged segment
                while prev.next:
                    prev = prev.next
                    
            step *= 2
            
        return dummy.next

    def split(self, head: Optional[ListNode], step: int) -> Optional[ListNode]:
        """Splits off a sublist of size 'step' from head and returns the remainder."""
        if not head:
            return None
            
        # Move up to step-1 positions
        for _ in range(step - 1):
            if head.next:
                head = head.next
            else:
                break
                
        # Detach the rest of the list
        remainder = head.next
        head.next = None
        return remainder

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Merges two sorted lists and returns the merged list head."""
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        tail.next = l1 if l1 else l2
        return dummy.next
