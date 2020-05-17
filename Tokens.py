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
TYPES
'''
INTEGER = "Int"
PLUS = "Plus"
MINUS = "Minus"
MUL = "Multiplication"
DIV = "Division"
LPAREN = "LeftParenthesis"
RPAREN = "RightParenthesis"

EOF = "EOF"
