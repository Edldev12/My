from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}                      # key -> (value, freq)
        self.freq_map = defaultdict(OrderedDict) # freq -> OrderedDict(key -> True)
        self.min_freq = 0

    def _update_frequency(self, key: str, value: int = None) -> int:
        """Helper to increment a key's frequency and reorder it in O(1)."""
        val, freq = self.cache[key]
        if value is not None:
            val = value  # Update value if provided by a put() call
            
        # 1. Remove from current frequency bucket
        del self.freq_map[freq][key]
        
        # 2. Clean up min_freq pointer if the current min bucket becomes empty
        if freq == self.min_freq and not self.freq_map[freq]:
            self.min_freq += 1
            
        # 3. Insert into the incremented frequency bucket
        new_freq = freq + 1
        self.cache[key] = (val, new_freq)
        self.freq_map[new_freq][key] = True
        return val

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self._update_frequency(key)

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # Scenario A: Key already exists. Update value and increment frequency.
        if key in self.cache:
            self._update_frequency(key, value)
            return

        # Scenario B: Capacity full. Evict the LFU (and LRU tie-breaker) key.
        if len(self.cache) >= self.capacity:
            # Pop the oldest (first) item from the min_freq bucket
            evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.cache[evict_key]

        # Scenario C: Insert new key. Initial frequency is always 1.
        self.cache[key] = (value, 1)
        self.freq_map[1][key] = True
        self.min_freq = 1  # Reset min frequency to 1 for the fresh item
