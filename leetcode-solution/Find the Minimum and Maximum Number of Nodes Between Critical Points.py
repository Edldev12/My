# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Need at least 3 nodes for a critical point
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        curr_idx = 1
        
        first_cp_idx = -1
        last_cp_idx = -1
        min_dist = float('inf')
        
        while curr.next:
            # Check if current node is local maxima or local minima
            is_max = curr.val > prev.val and curr.val > curr.next.val
            is_min = curr.val < prev.val and curr.val < curr.next.val
            
            if is_max or is_min:
                if first_cp_idx == -1:
                    first_cp_idx = curr_idx
                else:
                    # Update minimum distance using the adjacent critical point
                    min_dist = min(min_dist, curr_idx - last_cp_idx)
                
                # Update last seen critical point
                last_cp_idx = curr_idx
            
            # Move pointers forward
            prev = curr
            curr = curr.next
            curr_idx += 1
            
        # If fewer than 2 critical points were found
        if first_cp_idx == last_cp_idx:
            return [-1, -1]
            
        max_dist = last_cp_idx - first_cp_idx
        return [min_dist, max_dist]

        
