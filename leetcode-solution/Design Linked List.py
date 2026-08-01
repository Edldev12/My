class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        """
        Initializes the MyLinkedList object.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        """
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val as the last element of the linked list.
        """
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node. 
        If index equals the length of the linked list, append to the end.
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
            
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
            
        new_node = ListNode(val, curr.next)
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
            
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
            
        self.size -= 1
