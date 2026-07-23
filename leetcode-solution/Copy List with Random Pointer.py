
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Clone nodes and interweave them
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next, None)
            curr.next = new_node
            curr = new_node.next
            
        # Step 2: Assign random pointers to the cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # Step 3: Separate the original list and cloned list
        curr = head
        cloned_head = head.next
        while curr:
            cloned_curr = curr.next
            curr.next = cloned_curr.next
            curr = curr.next
            if cloned_curr.next:
                cloned_curr.next = cloned_curr.next.next
                
        return cloned_head
