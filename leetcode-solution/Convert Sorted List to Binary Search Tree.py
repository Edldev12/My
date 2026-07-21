# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
            
        # Use fast and slow pointers to locate the middle node
        # 'prev' is kept to disconnect the left half of the list
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # Disconnect the left half from the middle node
        if prev:
            prev.next = None
            
        # 'slow' is now the middle element and becomes the root
        root = TreeNode(slow.val)
        
        # Recursively construct left and right subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root
