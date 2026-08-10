# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If there's 0 or 1 node, no pairs exist to insert between
        if not head or not head.next:
            return head
        
        curr = head
        while curr and curr.next:
            # 1. Calculate GCD of adjacent nodes
            gcd_val = math.gcd(curr.val, curr.next.val)
            
            # 2. Create the new GCD node
            gcd_node = ListNode(gcd_val)
            
            # 3. Insert it between curr and curr.next
            gcd_node.next = curr.next
            curr.next = gcd_node
            
            # 4. Move curr to the original next node (now two steps ahead)
            curr = gcd_node.next
            
        return head
