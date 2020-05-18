from Tokens import *

class Lexer():
    def __init__(self):
        self.position = 0
        self.text = ""
        self.whitespace = [" ", "\n"]
        self.symbols = {
            "+": PLUS,
            "-": MINUS,
            "*": MUL,
            "/": DIV,
            "(": LPAREN,
            ")": RPAREN,
            ";": SEMI,
            "{": LCURL,
        }

        # This is used for syntax fixing
        self.cache = []

    def next_token(self) -> Token:
        # If the token cache is not empty, pop from it
        if len(self.cache) != 0:
            return self.cache.pop()

        while self.position < len(self.text):

            # Ignore whitespaces
            if self.get_current_char() in self.whitespace:
                self.advance()
                continue
            
            # Tokenize keywords and variables
            if self.get_current_char().isalpha():
                return self.get_name()

            # Tokenize numeric values 
            if self.get_current_char().isnumeric():
                return self.get_number()

            # Tokenize one char tokens
            for symbol in self.symbols.keys():
                if self.get_current_char() == symbol:
                    self.advance()
                    return Token(self.symbols[symbol], symbol)

            # For easier writing, the lexer will append a RightCurly with a semicolon
            if self.get_current_char() == "}":
                token = Token(RCURL, "}")
                if self.peek() != ";":
                    self.cache.append(Token(SEMI, ";"))
                self.advance()
                return token

            # Tokenize == and =
            if self.get_current_char() == "=":
                token = None
                if self.peek() == "=":
                    token = Token(EQTO, "==")
                    self.advance()
                else:
                    token = Token(ASSIGN, "=")
                self.advance()
                return token

            if self.get_current_char() == ">":
                token = None
                if self.peek() == "=":
                    token = Token(GETHAN, ">=")
                    self.advance()
                else:
                    token = Token(GTHAN, ">")
                self.advance()
                return token
            
            if self.get_current_char() == "<":
                token = None
                if self.peek() == "=":
                    token = Token(LETHAN, "<=")
                    self.advance()
                else:
                    token = Token(LTHAN, "<")
                self.advance()
                return token


        return Token(EOF, None)

    def peek(self)->str:
        return self.text[self.position+1]

    def advance(self):
        self.position+=1

    def get_current_char(self) -> str:
        return self.text[self.position]

    def get_number(self) -> Token:
        s = ""

        while self.position < len(self.text) and (self.get_current_char().isnumeric() or self.get_current_char() == "."):
            s += self.get_current_char()
            self.advance()
        
        if s.find(".") == -1:
            return Token(INTEGER, int(s))
        else:
            return Token(FLOAT, float(s))   

    def get_name(self) -> Token:
        s = ""

        while self.position < len(self.text) and (self.get_current_char().isalpha()):
            s += self.get_current_char()
            self.advance()   

        #Be aware - This line makes the syntax case-insensitive
        s = s.upper()
        if s in Keywords:
            return Token(s, s)
        else:
            return Token(ID, s) 

    def tokenize(self, text) -> list:
        self.text = text

        tokens = []
        current_token = self.next_token()
        while current_token.value != None:
            tokens.append(current_token)
            current_token = self.next_token()

        tokens.append(Token(EOF, None))

        return tokens



if __name__ == "__main__":
    teststr = "5 * (2 + 3)"
    tokenizer = Lexer()
    print(tokenizer.tokenize(teststr))    
