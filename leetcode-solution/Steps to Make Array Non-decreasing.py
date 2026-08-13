class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        # Stack stores tuples of (value, steps_needed_to_be_consumed)
        stack = []
        max_steps = 0
        
        # Traverse backwards from right to left
        for i in range(len(nums) - 1, -1, -1):
            cur_steps = 0
            
            # While the current element is strictly greater than the top of the stack
            while stack and nums[i] > stack[-1][0]:
                # It takes at least 1 step + whatever steps the popped element absorbed
                cur_steps = max(cur_steps + 1, stack[-1][1])
                stack.pop()
                
            stack.append((nums[i], cur_steps))
            max_steps = max(max_steps, cur_steps)
            
        return max_steps
