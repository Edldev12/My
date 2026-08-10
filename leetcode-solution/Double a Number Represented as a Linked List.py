# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. If head is 5 or greater, doubling creates a new leading 1
        if head.val >= 5:
            head = ListNode(0, head)
            
        curr = head
        while curr:
            # 2. Double the current digit and drop the carry portion
            curr.val = (curr.val * 2) % 10
            
            # 3. Look ahead: if next node triggers a carry, add 1 to current
            if curr.next and curr.next.val >= 5:
                curr.val += 1
                
            curr = curr.next
            
        return head
