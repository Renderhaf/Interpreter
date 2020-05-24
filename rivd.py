from Lexer import Lexer
from Parser import Parser
from Runner import Runner
import sys

def run_code(code: str):
    lexer = Lexer()
    tokens = lexer.tokenize(code)

    parser = Parser(tokens)
    node_tree = parser.parse()

    runner = Runner(node_tree)
    return runner.run()

if __name__ == "__main__":
    assert len(sys.argv) > 1
    with open(sys.argv[1], "r") as file:
        text = file.read()
    
    retval = run_code(text)
    print("Returned {}".format(retval))