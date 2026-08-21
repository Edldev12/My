lass Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    # Phase 1: Find the intersection point of the two runners
        tortoise = nums[0]
        hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
                
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        return hare

            
