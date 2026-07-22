class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        curr = root  # Loop through levels
        
        while curr:
            dummy = Node(0)  # Dummy head for the next level's linked list
            tail = dummy     # Tail to append discovered children
            
            # Traverse the current level like a linked list
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next  # Move to the next node on the current level
                
            # Move down to the start of the next level
            curr = dummy.next
            
        return root
