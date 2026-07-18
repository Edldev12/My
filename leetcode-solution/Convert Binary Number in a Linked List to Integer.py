# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        decimal_val = 0
        
        while head:
            # Shift existing bits left by 1 (multiply by 2) and add the new bit
            decimal_val = (decimal_val << 1) | head.val
            head = head.next
            
        return decimal_val
