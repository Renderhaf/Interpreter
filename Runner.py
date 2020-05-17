from Nodes import *
from Tokens import *

class Runner():
    def __init__(self, node_tree, debug = False):
       self.node_tree = node_tree
       self.debug = debug

    def run_node(self, node: Node):
        class_name = node.__class__.__name__
        runner_func = getattr(self, "run_{}".format(class_name), None)
        if runner_func != None:
            res = runner_func(node)
            return res
        else:
            raise NotImplementedError("The {} method is not implemented".format("run_{}".format(class_name)))

    def run_BinNode(self, node: BinNode):
        if self.debug:
            print("Running a BinNode -> [{} -- {} -- {}]".format(node.left, node.action, node.right))

        if node.action.type == PLUS:
            val = self.run_node(node.left) + self.run_node(node.right)
        elif node.action.type == MINUS:
            val = self.run_node(node.left) - self.run_node(node.right)
        elif node.action.type == MUL:
            val = self.run_node(node.left) * self.run_node(node.right)
        elif node.action.type == DIV:
            val = self.run_node(node.left) / self.run_node(node.right)

        return val

    def run_ValueNode(self, node: ValueNode):
        if self.debug:
            print("Running a value node -> [{}]".format(node.value))
        return node.value

    def run(self):
        return self.run_node(self.node_tree)

if __name__ == "__main__":
    runner = Runner(BinNode(1,2,3))

    runner.run_node(BinNode(1,2,3))