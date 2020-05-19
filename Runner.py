from Nodes import *
from Tokens import *

class Runner():
    def __init__(self, node_tree, infoLevel=0):
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
        '''
        Checks if the correct node runner exists, and if it does, it runs the node with it
        '''
        class_name = node.__class__.__name__
        runner_func = getattr(self, "run_{}".format(class_name), None)
        if runner_func != None:
            res = runner_func(node)
            return res
        else:
            raise NotImplementedError(
                "The {} method is not implemented".format("run_{}".format(class_name)))

    def run_BinNode(self, node: BinNode):
        '''
        Combines the two sides of the bin node with the action, and returns the value
        '''
        if self.infoLevel > 1:
            print(
                "Running a BinNode -> [{} -- {} -- {}]".format(node.left, node.action, node.right))

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

        # Logical Operations
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
        '''
        Returns the nodes value
        '''
        if self.infoLevel > 1:
            print("Running a value node -> [{}]".format(node.value))

        if node.token.type == ID:
            return self.globalVariableTable.get(node.value, 0)

        return node.value

    def run_SingleNode(self, node: SingleNode):
        '''
        returns a value generated from the value node and the action node
        '''
        if self.infoLevel > 1:
            print(
                "Running a single node -> [{}, {}]".format(node.node, node.action))

        if node.action.type == MINUS:
            return -1 * self.run_node(node.node)
        elif node.action.type == BANG:
            return 1 if self.run_node(node.node) == 0 else 0

    def run_AssignmentNode(self, node: AssignmentNode):
        '''
        This node assigns a value to a variable, or changes the variables value
        It does not return anything
        '''
        if self.infoLevel > 1:
            print(
                "Running an Assignment node -> [{} -- {} -- {}]".format(node.var, node.action, node.value))

        if node.action.type == ASSIGN:
            self.globalVariableTable[node.var.value] = self.run_node(
                node.value)

        return None

    def run_StatementListNode(self, node: StatementListNode):
        '''
        This node represents a block of code (eg: the code in a for loop, or in an if statement)
        It returns True if the running code resulted in a RETURN statement, so it can be passed up the tree

        For example, if a return statement is called inside an if statement, it will stop executing the if block,
        return True back into the statementlist node that ran the if, and it, too, will return.
        '''
        if self.infoLevel > 1:
            print("Running an Statement List Node ->")

        list_retval = False

        for statement in node.statements:
            node_retval = self.run_node(statement)

            if self.infoLevel > 2:
                print(
                    "Return Value for type {} is -> {}".format(statement.__class__.__name__, node_retval))

            # This needs to be == True because Strings and Ints eval to True
            if node_retval in [True, "BREAK"]:
                list_retval = node_retval
                break

        return list_retval

    def run_IfNode(self, node: IfNode):
        '''
        This node executes the logic of an if statement
        It also returns the return value of the statement list that ran, so that can be passed up the tree
        '''
        if self.infoLevel > 1:
            print("Running an If Node ->")

        if (self.run_node(node.condition) != 0):
            return_val = self.run_node(node.if_statement_list)
            return return_val
        elif (node.else_statement_list != None):
            return_val = self.run_node(node.else_statement_list)
            return return_val

    def run_ActionNode(self, node: ActionNode):
        '''
        This node executed an action
        it returns a value based on the action it runs
        '''
        if self.infoLevel > 1:
            print(
                "Running an Action Node -> ({} -> {})".format(node.action.type, node.value))

        if node.action.type == "RETURN":
            self.stack.append(self.run_node(node.value))
            # By returning true, this action results in a propogating return chain
            return True

        elif node.action.type == "BREAK":
            # TODO: this should be changed into a return_value class
            return "BREAK"

        elif node.action.type == "PRINT":
            val = self.run_node(node.value)
            print(val)
            return False

    def run_NoneType(self, null):
        # This is here to make the interpreter more stable
        # Cases where this is called are for example when an empty statement is parsed
        if self.infoLevel > 1:
            print("Running a NULL Node")
        return

    def run_ForNode(self, node: ForNode):
        if self.infoLevel > 1:
            print(
                "Running a ForNode -> ({} -> {})".format(node.init_statement, node.statement_list))

        # Get the init variables
        variable = node.init_statement.get("VAR").value
        startval = self.run_node(node.init_statement.get("START"))
        endval = self.run_node(node.init_statement.get("END"))

        retval = None

        # Make sure that the var is not taken
        if variable in self.globalVariableTable.keys():
            raise NameError(
                "The variable name {} is already taken.".format(variable))
        else:
            self.globalVariableTable[variable] = startval
            while self.globalVariableTable[variable] < endval:
                retval = self.run_node(node.statement_list)
                if retval or retval == "BREAK":
                    break
                self.globalVariableTable[variable] += 1

            self.globalVariableTable.pop(variable)

            if retval == "BREAK":
                return False
            else:
                return retval

    def run_WhileNode(self, node: WhileNode):
        if self.infoLevel > 1:
            print(
                "Running a WhileNode -> ({} -> {})".format(node.condition, node.statement_list))

        condition = node.condition

        retval = None

        while self.run_node(condition) == 1:
            retval = self.run_node(node.statement_list)
            if retval or retval == "BREAK":
                break

        if retval == "BREAK":
            return False
        else:
            return retval

    def run(self):
        self.run_node(self.node_tree)
        if self.infoLevel > 0:
            print("Global Variable Table at EOF is {}".format(
                self.globalVariableTable))
            print("Stack at EOF is {}".format(self.stack))

        return_value = self.stack.pop()
        return return_value
