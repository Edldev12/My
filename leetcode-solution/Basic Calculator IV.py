from collections import Counter
import re

class Poly(Counter):
    def __add__(self, other):
        res = Poly(self)
        for term, coeff in other.items():
            res[term] += coeff
        return res

    def __sub__(self, other):
        res = Poly(self)
        for term, coeff in other.items():
            res[term] -= coeff
        return res

    def __mul__(self, other):
        res = Poly()
        for term1, coeff1 in self.items():
            for term2, coeff2 in other.items():
                # Combine terms: combine and sort their variable tuples
                new_term = tuple(sorted(term1 + term2))
                res[new_term] += coeff1 * coeff2
        return res

    @classmethod
    def from_val(cls, token: str, eval_map: dict) -> 'Poly':
        # If it's a known variable, substitute its integer value
        if token in eval_map:
            return cls({(): eval_map[token]})
        # If it's a numeric constant
        elif token.isdigit():
            return cls({(): int(token)})
        # Otherwise, treat it as a free variable term with a coefficient of 1
        else:
            return cls({(token,): 1})


class Solution:
    def listOutputs(self, poly: Poly) -> list[str]:
        # Formats according to LeetCode criteria:
        # 1. Degree descending (-len(term))
        # 2. Lexicographical ascending (term)
        def sort_key(term):
            return (-len(term), term)
        
        sorted_terms = sorted([t for t, c in poly.items() if c != 0], key=sort_key)
        output = []
        
        for term in sorted_terms:
            coeff = poly[term]
            if not term:
                output.append(str(coeff))
            else:
                var_str = '*'.join(term)
                output.append(f"{coeff}*{var_str}")
        return output

    def basicCalculatorIV(self, expression: str, evalvars: list[str], evalints: list[int]) -> list[str]:
        eval_map = dict(zip(evalvars, evalints))
        
        # Standardize spaces around parentheses to split properly into clean tokens
        expr = expression.replace('(', ' ( ').replace(')', ' ) ')
        tokens = expr.split()
        
        ops = []
        output_queue = []
        precedence = {'+': 1, '-': 1, '*': 2}
        
        # Shunting-yard algorithm to convert infix to postfix notation
        for token in tokens:
            if token.isalnum():
                output_queue.append(Poly.from_val(token, eval_map))
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while ops and ops[-1] != '(':
                    output_queue.append(ops.pop())
                ops.pop()  # Pop the '('
            elif token in precedence:
                while ops and ops[-1] in precedence and precedence[ops[-1]] >= precedence[token]:
                    output_queue.append(ops.pop())
                ops.append(token)
                
        while ops:
            output_queue.append(ops.pop())
            
        # Postfix stack evaluation using the Poly class operators
        stack = []
        for token in output_queue:
            if isinstance(token, Poly):
                stack.append(token)
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                    
        return self.listOutputs(stack[0] if stack else Poly())
