# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverseList(head)
        current = head
        max_val = current.val
        
        while current and current.next:
            if current.next.val < max_val:
               
                current.next = current.next.next
            else:
                
                max_val = current.next.val
                current = current.next
                
        return self.reverseList(head)
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
