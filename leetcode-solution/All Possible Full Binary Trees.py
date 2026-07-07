# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        
        def backtrack(nodes):
            if nodes % 2 == 0:
                return []
            if nodes == 1:
                return [TreeNode(0)]
            if nodes in memo:
                return memo[nodes]
            
            res = []
            for i in range(1, nodes, 2):
                left_trees = backtrack(i)
                right_trees = backtrack(nodes - 1 - i)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            
            memo[nodes] = res
            return res
            
        return backtrack(n)
