from Nodes import *
from Tokens import *

class Runner():
    def __init__(self, node_tree, infoLevel = 0):
       self.node_tree = node_tree
       self.globalVariableTable = dict()

       '''
       Info Levels:
       0 - Return value
       1 - Print GVT at the end of running
       2 - Print Debugging messages
       '''
       self.infoLevel = infoLevel

    def run_node(self, node: Node):
        class_name = node.__class__.__name__
        runner_func = getattr(self, "run_{}".format(class_name), None)
        if runner_func != None:
            res = runner_func(node)
            return res
        else:
            raise NotImplementedError("The {} method is not implemented".format("run_{}".format(class_name)))

    def run_BinNode(self, node: BinNode):
        if self.infoLevel > 1:
            print("Running a BinNode -> [{} -- {} -- {}]".format(node.left, node.action, node.right))

        left_node = self.run_node(node.left)
        right_node = self.run_node(node.right)

        # Arithmatic Operations
        if node.action.type == PLUS:
            val = left_node + right_node
        elif node.action.type == MINUS:
            val = left_node - right_node
        elif node.action.type == MUL:
            val = left_node * right_node
        elif node.action.type == DIV:
            val = left_node / right_node

        #Logical Operations
        elif node.action.type == EQTO:
            val = 1 if left_node == right_node else 0
        elif node.action.type == GTHAN:
            val = 1 if left_node > right_node else 0
        elif node.action.type == GETHAN:
            val = 1 if left_node >= right_node else 0
        elif node.action.type == LTHAN:
            val = 1 if left_node < right_node else 0
        elif node.action.type == LETHAN:
            val = 1 if left_node <= right_node else 0

        return val

    def run_ValueNode(self, node: ValueNode):
        if self.infoLevel > 1:
            print("Running a value node -> [{}]".format(node.value))
        
        if node.token.type == ID:
            return self.globalVariableTable.get(node.value, 0)

        print("-========================{}".format(node.value))
        return node.value

    def run_SingleNode(self, node:SingleNode):
        if self.infoLevel > 1:
            print("Running a single node -> [{}, {}]".format(node.node, node.action))

        if node.action.type == MINUS:
            return -1 * self.run_node(node.node)

    def run_AssignmentNode(self, node:AssignmentNode):
        if self.infoLevel > 1:
            print("Running an Assignment node -> [{} -- {} -- {}]".format(node.var, node.action, node.value))

        if node.action.type == ASSIGN:
            self.globalVariableTable[node.var.value] = self.run_node(node.value)

    def run_StatementListNode(self, node:StatementListNode):
        if self.infoLevel > 1:
            print("Running an Statement List Node ->")

        for statement in node.statements:
            return_value = self.run_node(statement)
            if return_value != None:
                return return_value

    def run_IfNode(self, node: IfNode):
        if self.infoLevel > 1:
            print("Running an If Node ->")
        
        if (self.run_node(node.condition) != 0):
            self.run_node(node.statement_list)
            

    def run(self):
        return_value = self.run_node(self.node_tree)
        if self.infoLevel > 0:
            print("Global Variable Table at EOF is {}".format(self.globalVariableTable))

        return return_value

if __name__ == "__main__":
    runner = Runner(BinNode(1,2,3))

    runner.run_node(BinNode(1,2,3))
