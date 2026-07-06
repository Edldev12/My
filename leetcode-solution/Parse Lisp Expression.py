class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
        self.pos = 0
        return self.parse_expression(tokens, [])

    def parse_expression(self, tokens: list, scopes: list) -> int:
        token = tokens[self.pos]
        if token == '(':
            self.pos += 1 
            command = tokens[self.pos]
            self.pos += 1 
            new_scope = {}
            current_scopes = scopes + [new_scope]
            
            if command == 'add':
                val1 = self.parse_expression(tokens, current_scopes)
                val2 = self.parse_expression(tokens, current_scopes)
                self.pos += 1  
                return val1 + val2
                
            elif command == 'mult':
                val1 = self.parse_expression(tokens, current_scopes)
                val2 = self.parse_expression(tokens, current_scopes)
                self.pos += 1 
                return val1 * val2
                
            elif command == 'let':
                while True:
                    if tokens[self.pos + 1] == ')' or tokens[self.pos] == '(':
                        ans = self.parse_expression(tokens, current_scopes)
                        self.pos += 1  
                        return ans
                    var_name = tokens[self.pos]
                    self.pos += 1 
                    
                    var_val = self.parse_expression(tokens, current_scopes)
                    new_scope[var_name] = var_val
                    
        else:
            self.pos += 1 
            if token[0].isalpha():
                for scope in reversed(scopes):
                    if token in scope:
                        return scope[token]
            return int(token)
