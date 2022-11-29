# Convert input regex from infix to postfix expression for expression tree creation

# Create a class to represent an expression tree for e-NFA creation
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right