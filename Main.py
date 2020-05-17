from Lexer import Lexer
from Parser import Parser
from Runner import Runner

justAdd = "1 + 1" # 2
simpleExpression = "1 + 2 + 3 - 6 + 10" # 10
basicMul = "10 * 10 + 50" # 150
basicDiv = "25 / 5 " # 5
basicMath = "5 * (2 + 3)" # 25

def test_input(text:str):
    lexer = Lexer()
    tokens = lexer.tokenize(text)

    print(
    '''
    The lexer input was:
    {}
    
    The Tokenized output from it was:
    {}
    '''.format(text, tokens))

    parser = Parser(tokens)
    node_tree = parser.parse()

    print(
    '''
    The Parser then created this Node Tree:
    {}
    '''.format(node_tree)
    )

    runner = Runner(node_tree, True)
    print(
    '''
    The Runner ran the node tree, and came up with this result:
    {}
    '''.format(runner.run())
    )

if __name__ == "__main__":
    test_input(basicMath)
