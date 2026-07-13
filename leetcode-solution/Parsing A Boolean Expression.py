class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for char in expression:
            # Commas are structural separators; we can safely ignore them
            if char == ',':
                continue
                
            # Process sub-expression evaluation when a group closes
            if char == ')':
                seen = set()
                
                # Gather all boolean terms inside the current parentheses group
                while stack[-1] != '(':
                    seen.add(stack.pop())
                
                stack.pop()  # Remove the opening '('
                operator = stack.pop()  # Get the prefix operator ('!', '&', '|')
                
                # Evaluate based on operator rules
                if operator == '!':
                    # Seen contains exactly one element ('t' or 'f')
                    stack.append('t' if 'f' in seen else 'f')
                elif operator == '&':
                    # If any term is 'f', the entire AND group evaluates to False
                    stack.append('f' if 'f' in seen else 't')
                elif operator == '|':
                    # If any term is 't', the entire OR group evaluates to True
                    stack.append('t' if 't' in seen else 'f')
            else:
                stack.append(char)
                
        return stack[0] == 't'
