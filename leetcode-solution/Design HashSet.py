
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        # Use a prime number for the number of buckets to reduce collisions
        self.num_buckets = 769
        self.buckets = [None] * self.num_buckets

    def _hash(self, key: int) -> int:
        return key % self.num_buckets

    def add(self, key: int) -> None:
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key)
            return
        
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return  # Key already exists
            if not curr.next:
                break
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]
        if not curr:
            return
        
        # If the head node itself holds the key
        if curr.key == key:
            self.buckets[index] = curr.next
            return
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False
