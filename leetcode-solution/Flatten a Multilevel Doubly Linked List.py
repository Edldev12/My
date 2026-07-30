"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        curr = head
        while curr:
            # If there is no child, just move forward
            if not curr.child:
                curr = curr.next
                continue
            
            # Find the tail of the child list
            child_tail = curr.child
            while child_tail.next:
                child_tail = child_tail.next
            
            # Connect child_tail to curr.next if curr.next exists
            if curr.next:
                child_tail.next = curr.next
                curr.next.prev = child_tail
            
            # Connect curr to curr.child
            curr.next = curr.child
            curr.child.prev = curr
            
            # Clear the child pointer
            curr.child = None
            
            # Move to the next node
            curr = curr.next
            
        return head
