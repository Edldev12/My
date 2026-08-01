# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prefix_map = {}
        prefix_sum = 0
        
        # Pass 1: Map each running sum to its latest node
        curr = dummy
        while curr:
            prefix_sum += curr.val
            prefix_map[prefix_sum] = curr
            curr = curr.next
            
        # Pass 2: Connect nodes to skip zero-sum segments
        prefix_sum = 0
        curr = dummy
        while curr:
            prefix_sum += curr.val
            curr.next = prefix_map[prefix_sum].next
            curr = curr.next
            
        return dummy.next
