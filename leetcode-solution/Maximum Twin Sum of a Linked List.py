# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
            
        # Step 3: Find the maximum twin sum
        max_sum = 0
        start = head
        while prev:
            max_sum = max(max_sum, start.val + prev.val)
            start = start.next
            prev = prev.next
            
        return max_sum
