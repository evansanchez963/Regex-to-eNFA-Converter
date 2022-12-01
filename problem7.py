from validate_regex import is_regex_valid
from regex_to_tree import *

"""
    TEST CASES:
    [000]+[000].[111]
    ([000]+[000].[111])*.([000]+[333])
    ([100]+[001])*.[100]
"""

def main():
    #regex = input("Enter a regular expression: ")
    #regex = regex.replace(" ", "") # Remove whitespace from regex
    regex = "[000]+[000].[111]"
    #w = input("Enter a string w: ")

    # Validate regex, terminate program if regex is invalid
    if(is_regex_valid(regex)):
        print("Regex is valid. Proceeding...")
        print()
    else:
        print("Regex is not valid. Terminating...")
        print()
        return

    # Part 1: Convert regex to e-NFA
    postfix = infix_to_postfix(regex)
    print(*postfix, sep=" ")

    expression_tree = construct_expression_tree(postfix)
    #print()
    print(expression_tree.data)

    # Part 2: Remove e-moves from NFA

    # Part 3: Test if string w is accepted by e-free NFA


main()