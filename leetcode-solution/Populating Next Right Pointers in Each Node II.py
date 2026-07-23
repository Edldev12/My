
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # Start with the root level
        current = root
        dummy = Node(0)
        
        while current:
            tail = dummy # Tail tracks the building of the next level
            
            # Traverse horizontally across the current level
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                current = current.next # Move to the next sibling
            
            # Transition to the next level down
            current = dummy.next
            dummy.next = None # Reset the dummy pointer for the subsequent level
            
        return root
