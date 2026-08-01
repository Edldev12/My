# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # Step 1: Convert linked list to an array
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        # Step 2: Initialize the answer array and stack
        ans = [0] * len(nums)
        stack = []  # Stores indices
        
        # Step 3: Process elements with a monotonic stack
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                smaller_idx = stack.pop()
                ans[smaller_idx] = nums[i]
            stack.append(i)
            
        return ans
