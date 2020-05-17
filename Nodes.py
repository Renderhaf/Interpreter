from Tokens import *

class Node():
    pass

class BinNode():
    '''
    This node represents binary actions, for example: addition, subtraction, multiplication...
    '''
    def __init__(self, left, action, right):
        self.left:Node = left
        self.action:Token = action
        self.right:Node = right
        
    def __str__(self):
        return "BinNode({} , {} , {})".format(self.left, self.action, self.right)

    def __repr__(self):
        return self.__str__()

class ValueNode():
    '''
    This node represents a value, for example - 5
    '''
    def __init__(self, node):
        self.token:Token = node
        self.value = node.value

    def __str__(self):
        return "ValueNode({})".format(self.value)

class SingleNode():
    '''
    This node represents a one sided action, for example: making a number negative
    '''
    def __init__(self, node: Token, action: Token):
        self.node = node
        self.action = action

    def __str__(self):
        return "SingleNode({}, {})".format(self.node, self.action)

