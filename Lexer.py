from Tokens import *

class Lexer():
    def __init__(self):
        self.position = 0
        self.text = ""
        self.whitespace = [" ", "\n"]

    def next_token(self) -> Token:
        while self.position < len(self.text):
            if self.get_current_char() in self.whitespace:
                self.advance()
                continue

            if self.get_current_char().isnumeric():
                return self.get_number()

            if self.get_current_char() == "+":
                self.advance()
                return Token(PLUS, "+")

            if self.get_current_char() == "-":
                self.advance()
                return Token(MINUS, "-")

            if self.get_current_char() == "*":
                self.advance()
                return Token(MUL, "*")
            
            if self.get_current_char() == "/":
                self.advance()
                return Token(DIV, "/")

            if self.get_current_char() == "(":
                self.advance()
                return Token(LPAREN, "(")

            if self.get_current_char() == ")":
                self.advance()
                return Token(RPAREN, ")")

        return Token(EOF, None)

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