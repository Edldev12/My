class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        # Dummy head and tail nodes to avoid edge-case checks
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # Maps string key -> Node
        self.key_map = {}

    def _add_node_after(self, new_node: Node, ref_node: Node) -> None:
        """Helper to insert new_node immediately after ref_node."""
        new_node.prev = ref_node
        new_node.next = ref_node.next
        ref_node.next.prev = new_node
        ref_node.next = new_node

    def _remove_node_if_empty(self, node: Node) -> None:
        """Helper to delete a node if it no longer holds any keys."""
        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_map:
            # Key is new, Target count is 1
            first_node = self.head.next
            if first_node == self.tail or first_node.count > 1:
                new_node = Node(1)
                self._add_node_after(new_node, self.head)
                first_node = new_node
            
            first_node.keys.add(key)
            self.key_map[key] = first_node
        else:
            # Key exists, move to current_count + 1
            curr_node = self.key_map[key]
            next_node = curr_node.next
            
            if next_node == self.tail or next_node.count > curr_node.count + 1:
                new_node = Node(curr_node.count + 1)
                self._add_node_after(new_node, curr_node)
                next_node = new_node
                
            next_node.keys.add(key)
            self.key_map[key] = next_node
            
            curr_node.keys.remove(key)
            self._remove_node_if_empty(curr_node)

    def dec(self, key: str) -> None:
        # Guaranteed that key exists per constraints
        curr_node = self.key_map[key]
        curr_node.keys.remove(key)
        
        if curr_node.count == 1:
            del self.key_map[key]
        else:
            prev_node = curr_node.prev
            if prev_node == self.head or prev_node.count < curr_node.count - 1:
                new_node = Node(curr_node.count - 1)
                self._add_node_after(new_node, prev_node)
                prev_node = new_node
                
            prev_node.keys.add(key)
            self.key_map[key] = prev_node
            
        self._remove_node_if_empty(curr_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        # Return an arbitrary element from the max count bucket
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        # Return an arbitrary element from the min count bucket
        return next(iter(self.head.next.keys))
