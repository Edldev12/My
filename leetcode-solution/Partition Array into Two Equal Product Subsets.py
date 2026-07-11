class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        valid_nums = [x for x in nums if target % x == 0]
        if len(valid_nums) != len(nums):
            return False
            
        total_product = 1
        for x in nums:
            total_product *= x
        if total_product != target * target:
            return False

        n = len(nums)
        
        def dfs(index, current_product, count):
            if current_product == target:
                return 0 < count < n
            if index >= n or current_product > target:
                return False
            if dfs(index + 1, current_product * nums[index], count + 1):
                return True

            if dfs(index + 1, current_product, count):
                return True
                
            return False

        return dfs(0, 1, 0)
