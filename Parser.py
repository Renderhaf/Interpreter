from Tokens import *
from Nodes import *

class Parser():
    def __init__(self, token_list:list):
        self.token_list = token_list
        self.pos = 0
    
    def get_current_token(self)->Token:
        return self.token_list[self.pos]

    def advance(self)->None:
        self.pos += 1
    
    def parse_value(self)->ValueNode:
        '''
        This parses a value out of the tokens, and returns a ValueNode
        A Value has the highest precedence
        Value: INTEGER | LPAREN expression RPAREN
        '''
        if self.get_current_token().type == INTEGER:
            node = ValueNode(self.get_current_token())
            self.advance()
            return node 
            
    def parse_expression(self)->BinNode:
        '''
        An expression consists of:
        Expression: term PLUS | MINUS term
        '''
        left = self.parse_term()

        while self.get_current_token().type in [PLUS, MINUS]:
            action = self.get_current_token()
            self.advance()

            # Recursivly define the left node as the left node PLUS | MINUS the right node, and parse the right node
            # This way, in case of a long expression (ex: 4 + 3 + 2 + 1), the older nodes will be pushed left
            left = BinNode(left, action, self.parse_term())
        
        return left

    def parse_term(self)->BinNode:
        '''
        A term consists of:
        Term: value MUL | DIV value
        '''
        left = self.parse_value()

        while self.get_current_token().type in [MUL, DIV]:
            action = self.get_current_token()
            self.advance()

            left = BinNode(left, action, self.parse_value())
        
        return left

    def parse(self):
        return self.parse_expression()


