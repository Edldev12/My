class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        # Dictionary to track the day a specific state was first seen
        seen = {}
        
        for day in range(n):
            # Convert cells to a tuple so it can be used as a dictionary key
            state_tuple = tuple(cells)
            
            # If we detect a cycle, fast-forward the remaining days
            if state_tuple in seen:
                cycle_length = day - seen[state_tuple]
                remaining_days = (n - day) % cycle_length
                return self.prisonAfterNDays(cells, remaining_days)
            
            # Record the current state and the day we saw it
            seen[state_tuple] = day
            
            # Compute the state for the next day
            next_day_cells = [0] * 8
            for i in range(1, 7):
                # If neighbors are both 1s or both 0s, they are equal
                if cells[i - 1] == cells[i + 1]:
                    next_day_cells[i] = 1
                else:
                    next_day_cells[i] = 0
            
            cells = next_day_cells
            
        return cells
