from Lexer import Lexer
from Parser import Parser
from Runner import Runner

infoLevel = 0

basicMath = "-5 * (2 -- 3)" # 25
floatMath = "1.1 * 9 + 0.1" # 10

basicVar = "X"
basicAssignment = "X = 5 * 3 + 5;"

smallProgram = '''
    x = 15 / 3 + 5;
    b = 5 * x;
    return b;
    '''

ifProgram = '''
X = 5;
R = 0;
if (X == 5){
    R = 1;
} else {
    R = 0;
}

return R;
'''
with open("file.txt", "r") as file:
    fileProgram = file.read()

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

    runner = Runner(node_tree, infoLevel)
    print(
    '''
    The Runner ran the node tree, and came up with this result:
    {}
    '''.format(runner.run())
    )

if __name__ == "__main__":
    test_input(ifProgram)
