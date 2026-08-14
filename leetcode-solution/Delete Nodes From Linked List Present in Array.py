# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Convert list to set for O(1) lookups
        num_set = set(nums)
        
        # 2. Initialize a dummy node to seamlessly handle head deletion
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # 3. Traverse and skip nodes present in the set
        while current.next:
            if current.next.val in num_set:
                current.next = current.next.next  # Skip the node
            else:
                current = current.next             # Advance the pointer
                
        return dummy.next
