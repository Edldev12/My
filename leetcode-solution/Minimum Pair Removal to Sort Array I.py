class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        
        # Helper function to check if the array is already sorted non-decreasingly
        def is_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True
        
        # Continuously perform the operation until the array is sorted
        while not is_sorted(nums):
            min_sum = float('inf')
            target_index = -1
            
            # Find the leftmost adjacent pair with the minimum sum
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    target_index = i
            
            # Replace the pair at target_index with their combined sum
            nums[target_index] = min_sum
            nums.pop(target_index + 1)
            
            operations += 1
            
        return operations
