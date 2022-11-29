from validate_regex import is_regex_valid

def build_e_nfa(regular):
    # Read regex by one character at a time
    
    # Convert it from infix to postfix

    nfa = []    # Placeholder

    regular = regular.split()
    regular = "".join(regular)  # remove spaces

    for symbol in regular:
        print(symbol)
        # Build the nfa one symbol at a time here

    return nfa
    


def remove_e_moves(nfa):
    pass


def accepted(dfa, w):
    pass


def main():
    regex = input("Enter a regular expression: ")
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

    #e_nfa = build_e_nfa(regular)
    
    #remove e-moves

    #nfa = remove_e_moves(e_nfa)

    # test if w is accepted

    #res = accepted(nfa, w)


main()