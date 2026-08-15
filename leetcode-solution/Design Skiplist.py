import random

class SkiplistNode:
    def __init__(self, val: int, levels: int):
        self.val = val
        # forward[i] holds the reference to the next node at level i
        self.forward = [None] * levels

class Skiplist:
    def __init__(self):
        self.max_level = 16  # Accommodates 2^16 = 65,536 elements easily
        self.p = 0.5         # Coin flip probability
        self.head = SkiplistNode(-1, self.max_level)
        self.level = 1       # Current highest active level across the skiplist

    def _random_level(self) -> int:
        """Simulates geometric distribution via coin flips."""
        lvl = 1
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        curr = self.head
        # Start from the highest active level and move down
        for i in reversed(range(self.level)):
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        
        # Check the next node at the base level (level 0)
        curr = curr.forward[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        # update array stores the predecessor nodes at each level
        update = [None] * self.max_level
        curr = self.head
        
        for i in reversed(range(self.level)):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
            
        lvl = self._random_level()
        
        # If new level is higher than current active level, update global level
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl
            
        new_node = SkiplistNode(num, lvl)
        # Stitch the new node into the levels
        for i in range(lvl):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * self.max_level
        curr = self.head
        
        for i in reversed(range(self.level)):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
            
        curr = curr.forward[0]
        
        # If target element is not found, return False
        if curr is None or curr.val != num:
            return False
            
        # Unlink the node from all levels it belongs to
        for i in range(self.level):
            if update[i].forward[i] != curr:
                break
            update[i].forward[i] = curr.forward[i]
            
        # Re-calibrate the active global level if top levels become empty
        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1
            
        return True
