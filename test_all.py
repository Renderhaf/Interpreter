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

def test_types():
    code = '''
    a = 0.3;
    b = 0.7;
    c = 0.5;
    return (a+b+c);
    '''

    assert run_code(code) == 1.5


def test_for0():
    code = '''
    a = 0;
    for (i : 0 to 10){
        a = a + 1;
    }
    return a;
    '''

    assert run_code(code) == 10

def test_for1():
    code = '''
    a = 0;
    for (i : 0 to 10){
        a = a + i;
    }
    return a;
    '''

    assert run_code(code) == 45


def test_for2():
    code = '''
    a = 0;
    for (i : 0 to 10){
        a = a + 1;
        if (a == 5){
            return a;
        }
    }
    return 10;
    '''

    assert run_code(code) == 5

def test_break():
    code = '''
    a = 0;
    for (i : 0 to 101){
        a = a + 1;
        if (a == 50){
            break;
        }
    }
    return a;
    '''

    assert run_code(code) == 50

def test_nested_break():
    code = '''
    a = 0;
    for (i : 0 to 10){
        for (j : 0 to 10){
            a = a + 1;
            if (a >= 50){
                break;
            }
        }
    }
    return a;
    '''

    assert run_code(code) == 55

def test_while():
    code = '''
    a = 0;
    i = 0;

    while (i < 10){
        a = a + 1;
        i = i + 1;
    }

    return a;
    '''

    assert run_code(code) == 10

def test_comment():
    code = '''#return 5;#'''
    assert run_code(code) == None

def test_plusplusminusminus():
    code = '''
    a = 0;
    for (i : 0 to 10){
        a++;
    }
    a--;
    return a;
    '''

    assert run_code(code) == 9

def test_pluseqminuseq():
    code = '''
    a = 0;
    for (i : 0 to 10){
        a+=5;
    }
    a-=10;
    return a;
    '''

    assert run_code(code) == 40