from validate_regex import is_regex_valid
from regex_to_tree import infix_to_postfix, construct_expression_tree
from tree_to_NFA import build_eNFA

"""
    TEST CASES:
    [000]+[000].[111]
    ([000]+[000].[111])*.([000]+[333])
    ([100]+[001])*.[100]
    ([000]+e)
    ([100]+[011])*.([101].[100]+[000])*.([000]+e)
    [011].[101]*.[000]
"""

def main():
    regex = input("Enter a regular expression: ")
    regex = regex.replace(" ", "") # Remove whitespace from regex
    w = input("Enter a string w: ")
    w = w.replace(" ", "") # Remove whitespace from w
    print()

    # Split input string into an array
    d = "]"
    w = w.split(d)
    w.pop()
    for i in range(len(w)):
        w[i] += d

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
    expression_tree = construct_expression_tree(postfix)
    NFA = build_eNFA(expression_tree)

    # Part 2: Remove e-moves from NFA
    NFA.remove_e_moves()

    # Part 3: Test if string w is accepted by e-free NFA
    if NFA.accepts(w):
        print("String w is valid.")
    else:
        print("String w is invalid.")

main()