class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        
        def get_next(i: int) -> int:
            return (i + nums[i]) % n

        # Process each index as a potential cycle start
        for i in range(n):
            # Values > 1000 or < -1000 represent visited/invalid paths from previous runs
            if abs(nums[i]) > 1000:
                continue
                
            slow = i
            fast = i
            is_forward = nums[i] > 0
            
            # Unique marker for the current outer loop index path (e.g., 2000, 2001, etc.)
            marker = 2000 + i
            
            while True:
                # 1. Advance slow pointer by 1 step
                slow = get_next(slow)
                if abs(nums[slow]) > 1000 or (nums[slow] > 0) != is_forward:
                    break
                
                # 2. Advance fast pointer by 2 steps
                fast = get_next(fast)
                if abs(nums[fast]) > 1000 or (nums[fast] > 0) != is_forward:
                    break
                fast = get_next(fast)
                if abs(nums[fast]) > 1000 or (nums[fast] > 0) != is_forward:
                    break
                    
                # 3. Check if they meet
                if slow == fast:
                    # Valid cycles must have a length greater than 1
                    if slow == get_next(slow):
                        break
                    return True
            
            # Safe Path Cleaning: Mark all elements in this failed path with our unique marker
            # This completely avoids infinite cleaning loops
            curr = i
            while (nums[curr] > 0) == is_forward and abs(nums[curr]) <= 1000:
                nxt = get_next(curr)
                nums[curr] = marker
                curr = nxt
                
        return False
