

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
    regular = "a*b*"
    w = "aaabb"
    # regular = input()
    # w = input()

    # Convert regular into an e-NFA

    e_nfa = build_e_nfa(regular)
    
    # remove e-moves

    nfa = remove_e_moves(e_nfa)

    # test if w is accepted

    res = accepted(nfa, w)


main()