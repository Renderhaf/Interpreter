from Lexer import Lexer
from Parser import Parser
from Runner import Runner

def run_code(code: str):
    lexer = Lexer()
    tokens = lexer.tokenize(code)

    parser = Parser(tokens)
    node_tree = parser.parse()

    runner = Runner(node_tree,1)
    runner.run()

def test_math():
    code = """
    a = 5;
    b = 10;
    c = a + b;
    return c;
    """

    print(run_code(code))

test_math()