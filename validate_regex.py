"""
    ARGS:
    1: regex - A string representing a regex

    DESCRIPTION: Returns true if parentheses are balanced in expression, false if not.
"""
def are_paren_balanced(regex):
    stack = []

    for char in regex:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if (len(stack) == 0 or stack[len(stack) - 1] != "("):
                return False
            else:
                stack.pop()

    if (len(stack) == 0): 
        return True
    return False





"""
    ARGS:
    1: operand - A string representing an operand in the form of [000] through [999]

    DESCRIPTION: Returns true if the operand is in the correct form, false if not.
"""
def check_operand(operand):
    if(len(operand) < 5):
        return False

    for i in range(len(operand)):
        if i == 0 and operand[i] != "[":
            return False
        elif (i >= 1 and i <= 3) and not operand[i].isdigit():
            return False
        elif i == 4 and operand[i] != "]":
            return False
        elif i == 5 and operand[i] not in [".", "U", "*", ")"]:
            return False
    
    return True





"""
    ARGS:
    1: regex - A string representing a regex

    DESCRIPTION: Returns true if operands are in the correct form in regex, false if not.
"""
def are_operands_valid(regex):
    # Check if each '[' is followed by 3 integers and a closing bracket
    for i in range(len(regex)):
        if regex[i] == "[":
            if not check_operand(regex[i:i+6]):
                return False
    
    return True






"""
    ARGS:
    1: regex - A string representing a regex

    DESCRIPTION: Returns true if operators are in the correct places in regex, false if not.
    Checks the left and right sides of operators such as 'U', '.', and '*'.
"""
def are_operators_valid(regex):
    for i in range(len(regex)):
        # Check left and right sides of 'U' and '.' and left side of '*'
        if regex[i] == "U":
            if i == len(regex) - 1:
                return False
            elif regex[i - 1] not in ["]", ")", "*"]: 
                return False
            elif regex[i + 1] not in ["[", "("]:
                return False
        elif regex[i] == ".":
            if i == len(regex) - 1:
                return False
            elif regex[i - 1] not in ["]", ")", "*"]: 
                return False
            elif regex[i + 1] not in ["[", "("]:
                return False
        elif regex[i] == "*":
            if regex[i - 1] not in ["]", ")"]:
                return False

    return True





"""
    ARGS:
    1: regex - A string representing a regex

    DESCRIPTION: Returns true if regex is valid, false if not
"""
def is_regex_valid(regex):
    paren_balanced = are_paren_balanced(regex)
    operands_valid = are_operands_valid(regex)
    operators_valid = are_operators_valid(regex)

    if (paren_balanced):
        print("The parentheses are valid.")
    else:
        print("The parentheses are invalid.")

    if (operands_valid):
        print("The operands are valid.")
    else:
        print("The operands are invalid.")

    if (operators_valid):
        print("The operators are valid.")
    else:
        print("The operators are invalid.")

    return paren_balanced and operands_valid and operators_valid