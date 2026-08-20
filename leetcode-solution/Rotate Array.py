class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k > n
        
        # Helper function to reverse a slice in-place
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        # 1. Reverse total array
        reverse(0, n - 1)
        # 2. Reverse first k elements
        reverse(0, k - 1)
        # 3. Reverse remaining elements
        reverse(k, n - 1)
