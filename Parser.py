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
        Value: INTEGER | LPAREN expression RPAREN | FLOAT | ID | Keyword
        '''
        if self.get_current_token().type in NUMERIC or self.get_current_token().type == ID:
            node = ValueNode(self.get_current_token())
            self.advance()
            return node 

        if self.get_current_token().type == LPAREN:
            self.advance() #In order to move into the parentheses
            node = self.parse_expression()
            self.advance() #In order to move out of the parentheses
            return node

        if self.get_current_token().type == MINUS:
            self.advance()
            node = SingleNode(self.parse_value(), Token(MINUS, "-"))
            return node

        
    def parse_expression(self)->BinNode:
        '''
        An expression consists of:
        Expression: term PLUS | MINUS | EQTO | GTHAN | GETHAN | LTHAN | LETHAN term
        '''
        left = self.parse_term()

        while self.get_current_token().type in [PLUS, MINUS, EQTO, GTHAN, GETHAN, LTHAN, LETHAN]:
            action = self.get_current_token()
            self.advance()

            # Recursivly define the left node as the left node PLUS | MINUS the right node, and parse the right node
            # This way, in case of a long expression (ex: 4 + 3 + 2 + 1), the older nodes will be pushed left
            left = BinNode(left, action, self.parse_term())
        
        return left

    def parse_term(self)->BinNode:
        '''
        A term consists of:
        Term: value MUL | DIV value || value
        '''
        left = self.parse_value()

        while self.get_current_token().type in [MUL, DIV]:
            action = self.get_current_token()
            self.advance()

            left = BinNode(left, action, self.parse_value())
        
        return left


    def parse_program(self)->StatementListNode:
        '''
        Parses a program. A program consists of statements, sepereated by semicolons
        '''

        compound = StatementListNode()
        statements = [self.parse_statement()]

        while self.get_current_token().type == SEMI:
            self.advance()

            if self.get_current_token().type != EOF:
                statements.append(self.parse_statement())

        compound.statements.extend(statements)

        return compound


    def parse_statement(self):
        '''
        A statement consists of:
        Statement: assignment 
        '''
        if self.get_current_token().type == ID:

            var = self.get_current_token()
            self.advance()
            action = self.get_current_token()
            self.advance()

            if action.type == ASSIGN:
                return AssignmentNode(var, action, self.parse_expression())

        elif self.get_current_token().type in Keywords:
            keyword = self.get_current_token()

            if keyword.type == "RETURN":
                self.advance()
                return_value = self.get_current_token()
                return ValueNode(return_value)


    def parse(self):
        return self.parse_program()


