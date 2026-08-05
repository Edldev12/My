# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Base case: if the tree is empty, we cannot find the path
        if not root:
            return False
            
        # Check if the current tree node can start a matching path,
        # or if the path exists in the left or right subtrees
        return (self.check_match(head, root) or 
                self.isSubPath(head, root.left) or 
                self.isSubPath(head, root.right))
        
    def check_match(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Base case: if we successfully reached the end of the list, a match is found
        if not head:
            return True
        # If the tree ends before the list finishes, it's a mismatch
        if not root:
            return False
        # If current values mismatch, this path fails
        if head.val != root.val:
            return False
            
        # Continue validating consecutively down either the left or right branch
        return (self.check_match(head.next, root.left) or 
                self.check_match(head.next, root.right))
