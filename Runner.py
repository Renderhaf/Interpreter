from Nodes import *
from Tokens import *

class Runner():
    def __init__(self, node_tree, infoLevel = 0):
       self.node_tree = node_tree
       self.globalVariableTable = dict()
       self.stack = []

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
        elif node.action.type == NEQTO:
            val = 1 if left_node != right_node else 0
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

        return node.value

    def run_SingleNode(self, node:SingleNode):
        if self.infoLevel > 1:
            print("Running a single node -> [{}, {}]".format(node.node, node.action))

        if node.action.type == MINUS:
            return -1 * self.run_node(node.node)
        elif node.action.type == BANG:
            return 1 if self.run_node(node.node) == 0 else 0

    def run_AssignmentNode(self, node:AssignmentNode):
        if self.infoLevel > 1:
            print("Running an Assignment node -> [{} -- {} -- {}]".format(node.var, node.action, node.value))

        if node.action.type == ASSIGN:
            self.globalVariableTable[node.var.value] = self.run_node(node.value)

    def run_StatementListNode(self, node:StatementListNode):
        if self.infoLevel > 1:
            print("Running an Statement List Node ->")

        has_returned = False

        for statement in node.statements:
            is_return = self.run_node(statement)

            if self.infoLevel > 2:
                print("Return Value for type {} is -> {}".format(statement.__class__.__name__, is_return))

            if is_return: 
                has_returned = True
                break

        if not node.isFunction:
            return has_returned

    def run_IfNode(self, node: IfNode):
        if self.infoLevel > 1:
            print("Running an If Node ->")
        
        if (self.run_node(node.condition) != 0):
            return_val = self.run_node(node.statement_list)
            return return_val
            
    def run_ActionNode(self, node: ActionNode):
        if self.infoLevel > 1:
            print("Running an Action Node -> ({} -> {})".format(node.action.type, node.value))

        if node.action.type == "RETURN":
            self.stack.append(self.run_node(node.value))
            return True

    def run_NoneType(self, none):
        #This is here to make the interpreter more stable
        #Cases where this is called are for example when an empty statement is parsed
        return

    def run(self):
        self.run_node(self.node_tree)
        if self.infoLevel > 0:
            print("Global Variable Table at EOF is {}".format(self.globalVariableTable))
            print("Stack at EOF is {}".format(self.stack))

        return_value = self.stack.pop()
        return return_value

if __name__ == "__main__":
    runner = Runner(BinNode(1,2,3))

    runner.run_node(BinNode(1,2,3))
