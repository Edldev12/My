import random

# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        # Store the head pointer to traverse from the start during each call
        self.head = head

    def getRandom(self) -> int:
        res = self.head.val
        curr = self.head
        i = 1
        
        while curr:
            # Generate a random integer between 1 and i (inclusive)
            if random.randint(1, i) == i:
                res = curr.val
            curr = curr.next
            i += 1
            
        return res
