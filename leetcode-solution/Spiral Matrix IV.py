# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize the matrix completely filled with -1
        matrix = [[-1] * n for _ in range(m)]
        
        # Start at the top-left cell
        r, c = 0, 0
        # Initial direction is moving right: row change = 0, col change = 1
        dr, dc = 0, 1
        
        curr = head
        while curr:
            # Place the current node's value into the matrix
            matrix[r][c] = curr.val
            curr = curr.next
            
            # Calculate what the next cell would be in the current direction
            next_r, next_c = r + dr, c + dc
            
            # If the next cell is out of bounds OR already filled (not -1), change direction
            if not (0 <= next_r < m and 0 <= next_c < n and matrix[next_r][next_c] == -1):
                # Clockwise rotation formula for directions: (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
                dr, dc = dc, -dr
            
            # Move to the valid next cell
            r += dr
            c += dc
            
        return matrix
