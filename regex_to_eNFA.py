"""
    ARGS:
    1: regex - A string representing a regex

    DESCRIPTION: Returns the postfix form of a regex represented by an array of strings. 
    This is used for creating the expression tree.
"""
def infix_to_postfix(regex):
    precedence_dict = {
        "": 0,
        "(": 1,
        "U": 2,
        ".": 3,
        "*": 4
    }

    postfix = []
    stack = []

    for i in range(len(regex)):
        curr_char = regex[i]

        if curr_char.isdigit() or curr_char == "]":
            continue
        elif curr_char == "[":
            operand = regex[i:i+5]
            postfix.append(operand)
        elif curr_char == "(":
            stack.append("(")
        elif curr_char == ")":
            top = stack[len(stack)-1]
            while top != "(":
                operator = stack.pop()
                top = stack[len(stack)-1]
                if operator != "(":
                    postfix.append(operator)
            stack.pop()
        elif curr_char in ["U", ".", "*"]:
            if len(stack) == 0:
                stack.append(curr_char)
            else:
                top = stack[len(stack)-1]
                if precedence_dict[top] >= precedence_dict[curr_char]:
                    while precedence_dict[top] >= precedence_dict[curr_char]:
                        operator = stack.pop()
                        if len(stack) == 0:
                            top = ""
                        else:
                            top = stack[len(stack)-1]
                        postfix.append(operator)
                        stack.append(curr_char)
                else:
                    stack.append(curr_char)
    
    while len(stack) != 0:
        operator = stack.pop()
        postfix.append(operator)

    return postfix





"""
    Create a binary tree to store an expression tree.
    This is used for constructing the e-NFA.
"""
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right





"""
    ARGS:
    1: postfix - An array of strings representing a postfix expression for a regex

    DESCRIPTION: Constructs and returns an expression tree.
"""
def construct_expression_tree(postfix):

    if not postfix:
        return

    # Initialize a stack to store tree pointers
    stack = []

    for str in postfix:
        # If the operators are union or concatenation, they will always be parents with two children being operands
        if str == "U" or str == ".":
            y = stack.pop()
            x = stack.pop()

            # Create a new binary tree where the root is the operator and 
            # its left and right children points to x and y respectively
            node = Node(str, x, y)

            stack.append(node)
        # If the operator is a kleene star, it will be a parent with only one operand child on its left subtree 
        elif str == "*":
            x = stack.pop()

            # Create a new binary tree where the root is the operator and 
            # its left and right children points to x and y respectively
            node = Node(str, x)

            stack.append(node)
        # If the current token is an operand, create a new node with the operand as a root
        # and push it to the stack
        else:
            stack.append(Node(str))

    # The remaining element on the stack is the root node
    return stack[0]





"""
    ARGS:
    1: root - The root node of an expression tree

    DESCRIPTION: Prints an infix expression for a binary tree
"""
def inorder_traversal(root):
    if root is None:
        return

    # if the current token is an operator, print open parenthesis
    if root.data in ["U", ".", "*"]:
        print("(", end="")
    
    inorder_traversal(root.left)
    print(root.data, end="")
    inorder_traversal(root.right)

    if root.data in ["U", ".", "*"]:
        print(")", end="")