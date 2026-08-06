# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Find the k-th node from the beginning
        first = head
        for _ in range(k - 1):
            first = first.next
            
        # Step 2: Use a fast pointer to locate the k-th node from the end
        fast = first
        second = head
        while fast.next:
            fast = fast.next
            second = second.next
            
        # Step 3: Swap the values of the two targeted nodes
        first.val, second.val = second.val, first.val
        
        return head
