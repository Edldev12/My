
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Dummy node simplifies edge cases like updating the head
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # Find the kth node of the current group
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break
                
            group_next = kth.next
            
            # Reverse the current group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # Update pointers to fix the surrounding connections
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
            
        return dummy.next

    def getKthNode(self, curr: ListNode, k: int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
