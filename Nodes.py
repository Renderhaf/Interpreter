from Tokens import *

class Node():
    pass

class BinNode():
    def __init__(self, left, action, right):
        self.left:Node = left
        self.action:Token = action
        self.right:Node = right
        
    def __str__(self):
        return "BinNode({} , {} , {})".format(self.left, self.action, self.right)

    def __repr__(self):
        return self.__str__()

class ValueNode():
    def __init__(self, node):
        self.token:Token = node
        self.value = node.value

    def __str__(self):
        return "ValueNode({})".format(self.value)