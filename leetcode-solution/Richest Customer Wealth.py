class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth=0
        for customer in accounts:
            currentwealth=sum(customer)
            if currentwealth > maxwealth:
                maxwealth = currentwealth
        return maxwealth
