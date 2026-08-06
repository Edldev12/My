# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Step 1: Find the (a-1)-th node and the (b+1)-th node in list1
        curr = list1
        for i in range(b + 1):
            if i == a - 1:
                start_node = curr
            curr = curr.next
        end_node = curr  # This is the (b+1)-th node
        
        # Step 2: Connect the (a-1)-th node to the head of list2
        start_node.next = list2
        
        # Step 3: Find the tail of list2
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
            
        # Step 4: Connect the tail of list2 to the (b+1)-th node
        tail2.next = end_node
        
        return list1
