# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            if curr.left:
                # Find the rightmost node of the left subtree
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Rewire the right subtree to the rightmost node
                rightmost.right = curr.right
                
                # Move the left subtree to the right
                curr.right = curr.left
                curr.left = None
                
            # Move to the next node in the flattened path
            curr = curr.right
