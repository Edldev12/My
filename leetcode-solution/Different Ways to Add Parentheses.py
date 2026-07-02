class Solution:

    def diffWaysToCompute(self, expression: str) -> list[int]:
        # Memoization dictionary to store the results of sub-expressions
        memo = {}

        def backtrack(expr):
            if expr in memo:
                return memo[expr]

            res = []
            for i in range(len(expr)):
                char = expr[i]
                if char in "+-*":
                    # Divide the expression at the operator
                    left = backtrack(expr[:i])
                    right = backtrack(expr[i + 1 :])

                    # Conquer: Combine results from left and right
                    for l in left:
                        for r in right:
                            if char == "+":
                                res.append(l + r)
                            elif char == "-":
                                res.append(l - r)
                            elif char == "*":
                                res.append(l * r)

            # If the expression is just a number (no operators)
            if not res:
                res.append(int(expr))

            memo[expr] = res
            return res

        return backtrack(expression)
