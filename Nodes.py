from Tokens import *

class Node():
    pass

class BinNode(Node):
    '''
    This node represents binary actions, for example: addition, subtraction, multiplication...
    '''
    def __init__(self, left, action, right):
        self.left:Node = left
        self.action:Token = action
        self.right:Node = right
        
    def __str__(self):
        return "BinNode({} , {} , {})".format(self.left, self.action, self.right)

class ValueNode(Node):
    '''
    This node represents a value, for example - 5
    '''
    def __init__(self, node):
        self.token:Token = node
        self.value = node.value

    def __str__(self):
        return "ValueNode({})".format(self.value)

class SingleNode(Node):
    '''
    This node represents a one sided action, for example: making a number negative
    '''
    def __init__(self, node: Token, action: Token):
        self.node = node
        self.action = action

    def __str__(self):
        return "SingleNode({}, {})".format(self.node, self.action)

class StatementListNode(Node):
    '''
    This node represents a list of statements, seperated by ;
    '''
    def __init__(self):
        self.statements = []
    
    def __str__(self):
        return "StatementList({})".format(self.statements)

class AssignmentNode(Node):
    '''
    This node represents an assignment to a variable
    '''
    def __init__(self, var, action, value):
        self.var:Token = var
        self.action:Token = action
        self.value:Node = value

    def __str__(self):
        return "AssignmentNode({} , {} , {})".format(self.var, self.action, self.value)

    def __repr__(self):
        return self.__str__()

# class ActionNode(Node):
#     '''
#     This node represents an action, for example: print x
#     '''

        