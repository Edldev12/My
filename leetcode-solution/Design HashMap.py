class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap: # The judge needs this exact class name
    def __init__(self):
        self.num_buckets = 769
        self.buckets = [None] * self.num_buckets

    def _hash(self, key: int) -> int:
        return key % self.num_buckets

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key, value)
            return
        
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                curr.value = value  
                return
            if not curr.next:
                break
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self._hash(key)
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]
        if not curr:
            return
        
        if curr.key == key:
            self.buckets[index] = curr.next
            return
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

