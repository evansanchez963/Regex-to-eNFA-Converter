from validate_regex import is_regex_valid
from regex_to_eNFA import *


# Part 1
# Takes a string as an input and returns an e-nfa as an output
def build_e_nfa(regular):
    # Read regex by one character at a time
    
    # Convert it from infix to postfix

    #nfa = Node()    # Placeholder

    regular = regular.split()
    regular = "".join(regular)  # remove spaces

    li = []
    bracket = False
    operand = ""
    for i in regular:
        if i == '[':
            bracket = True
        elif bracket:
            if (i == ']'):
                bracket = False
                li.append(operand)
                operand = ""
            else:
                operand += i
        else:
            li.append(i)

    index = find_low_operation(li)

    print(li)
    print(index)

    return 0


# Returns first index of lowest operation
def find_low_operation(array):

    order_of_op = ['*', '.', 'U']

    para = False
    para_location = []

    for op in order_of_op:
        for i, val in enumerate(array):
            if val == '(':
                para = True
                para_location.append(i)
            elif not para:
                if op == val:
                    return i
            else:
                if val == ')':
                    para = False
                    para_location.append(i)

    while len(para_location) >= 2:
        n = find_low_operation(array[para_location[0]+1:para_location[1]-1]) + para_location[0] + 1
        para_location.pop(0)
        para_location.pop(0)
        if n:
            return n
    
    return 0
            


def build_helper(node, array):
    index = find_low_operation(array)

    # TODO Finish Resursive Node Builder
    

# Part 2
# Takes an e_nfa as an input and returns an e-free nfa as an output
def remove_e_moves(e_nfa):
    nfa = Node()
    
    return nfa

# Part 3
# Takes an nfa and a string as an input and returns a boolean as the output
# True if w is accepted by the nfa





def accepted(nfa, w):
    pass


def main():
    #regex = input("Enter a regular expression: ")
    regex = "[000].[123]" # [ "000", ".", "123" ]
    regex = "([000] U [000].[111])*.([000] U [222])"    
    regex = regex.replace(" ", "") # Remove whitespace from regex
    print("REGEX:", regex)
    #w = input("Enter a string w: ")

    # Validate regex, terminate program if regex is invalid
    if(is_regex_valid(regex)):
        print("Regex is valid. Proceeding...")
        print()
    else:
        print("Regex is not valid. Terminating...")
        print()

    # Convert regular into an e-NFA

    e_nfa = build_e_nfa(regex)
    
    # remove e-moves

    #nfa = remove_e_moves(e_nfa)

    # test if w is accepted

    # res = accepted(nfa, w)


main()