# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
            
        # Step 2: Determine sizes for each part
        base_size = length // k
        remainder = length % k
        
        result = []
        curr = head
        
        # Step 3: Extract each of the k parts
        for i in range(k):
            part_head = curr
            
            # Calculate size for current part
            # First 'remainder' parts get 1 extra node
            current_part_size = base_size + (1 if i < remainder else 0)
            
            # Traverse to the end of the current part
            for _ in range(current_part_size - 1):
                if curr:
                    curr = curr.next
            
            # Sever the link to isolate the current part
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
                
            result.append(part_head)
            
        return result
