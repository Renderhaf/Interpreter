class Token():
    def __init__(self, token_type:str, value):
        self.type = token_type
        self.value = value
    
    def get_int(self)->int:
        return int(self.value)

    def __str__(self)->str:
        return "Token({}, '{}')".format(self.type, self.value)

    def __repr__(self):
        return self.__str__()

'''
TOKEN TYPES
'''

#Data types
INTEGER = "Int"
FLOAT = "Float"

#Operators
PLUS = "Plus"
MINUS = "Minus"
MUL = "Multiplication"
DIV = "Division"
ASSIGN = "AssignmentEquals"

#Parenthesese
LPAREN = "LeftParenthesis"
RPAREN = "RightParenthesis"

#END OF FILE
EOF = "EOF"

#Variable ID for the Global Variable Table
ID = "ID"

SEMI = "Semicolon"


'''
DATA TYPE CATEGORIES
'''

NUMERIC = [INTEGER, FLOAT]

'''
KEYWORDS
'''

Keywords = [
    "FOR", "IF", "RETURN"
]
