from Lexer import Lexer
from Parser import Parser
from Runner import Runner

def run_code(code: str):
    lexer = Lexer()
    tokens = lexer.tokenize(code)

    parser = Parser(tokens)
    node_tree = parser.parse()

    runner = Runner(node_tree)
    return runner.run()

def test_math():
    code = """
    a = 5;
    b = 10;
    return (a+b);
    """

    assert run_code(code) == 15

def test_if():
    code = """
    a = 5;
    b = 10;
    statement = (a < b) + !(b < a) + (a != b);
    if (statement == 3){
        return 37;
    }
    return 10;
    """

    assert run_code(code) == 37

def test_nested_ifs():
    code = """
    a = 5;
    b = 10;
    if (a < b){
        if (a != b){
            return 37;
        }
        return 10;
    }
    return 10;
    """

    assert run_code(code) == 37


def test_if_else():
    code = """
    a = 5;
    b = 10;
    if (a == b){
        return 10;
    } else {
        return 37;
    }
    return 10;
    """

    assert run_code(code) == 37

