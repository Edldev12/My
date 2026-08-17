import heapq

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        # Pointers simulating a Doubly-Linked List
        L = [i - 1 for i in range(n)]
        R = [i + 1 for i in range(n)]
        R[-1] = -1  
        
        violations = 0
        heap = []
        
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                violations += 1
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))
            
        if violations == 0:
            return 0
            
        operations = 0
        
        while heap and violations > 0:
            s, u = heapq.heappop(heap)
            v = R[u]
            
            # Lazy deletion check
            if v == -1 or nums[u] + nums[v] != s:
                continue
                
            operations += 1
            
            p = L[u]
            nxt = R[v]
            
            # Subtract old violations
            if p != -1 and nums[p] > nums[u]:
                violations -= 1
            if nums[u] > nums[v]:
                violations -= 1
            if nxt != -1 and nums[v] > nums[nxt]:
                violations -= 1
                
            # Merge elements
            nums[u] = s
            R[u] = nxt
            if nxt != -1:
                L[nxt] = u
                
            # Add new violations and update heap
            if p != -1:
                if nums[p] > nums[u]:
                    violations += 1
                heapq.heappush(heap, (nums[p] + nums[u], p))
                
            if nxt != -1:
                if nums[u] > nums[nxt]:
                    violations += 1
                heapq.heappush(heap, (nums[u] + nums[nxt], u))
                
            if violations == 0:
                return operations
                
        return operations
