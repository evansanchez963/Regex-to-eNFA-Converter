STATE_COUNT = 0

def increment_state_count():
    global STATE_COUNT
    STATE_COUNT += 1





"""
    This is an NFA class that stores the e-NFA and NFA of a given regex.
    Properties:
        1: start_state - An integer representing a starting state
        2: accepting_states - An array of integers that represent accepting states
        3: transitions - A dictionary of dictionaries where the key is an integer representing a state
        and the value is another dictionary. In those dictionaries, the key is a key in the alphabet
        and the value is a set of integers representing which states it transfers to.
        Example: {0: {'[000]': {0, 1}, '[111]': {0}}} means that starting from state 0, input [000] transitions
        to state 0 and state 1, and input [111] transitions to state 1.
"""
class NFA:
    def __init__(self, start_state=None, accepting_states=None, transitions=None):
        self.start_state = start_state
        self.accepting_states = accepting_states
        self.transitions = transitions





"""
    ARGS:
    1: operand - An operand to be converted into an NFA

    DESCRIPTION: Creates an nfa for an operand. Creates a new start state and end state
    where the transition from the start state to the end state is the given operand.
"""
def operand_NFA(operand):
    start_state = 0
    accepting_states = []
    transitions = {}

    # Create a new start state
    new_start_state = STATE_COUNT
    increment_state_count()
    start_state = new_start_state

    # Create a new accepting state
    new_accepting_state = STATE_COUNT
    increment_state_count()
    accepting_states.append(new_accepting_state)

    # Create a transition (operand) from start state to new accepting state
    transitions[start_state] = {operand: {new_accepting_state}}

    return NFA(start_state, accepting_states, transitions)





"""
    ARGS:
    1: nfa_a - An NFA object to be operated on
    2: nfa_b - An NFA object to be operated on

    DESCRIPTION: Creates and returns a new NFA from the union of nfa_a and nfa_b.
"""
def union(nfa_a, nfa_b):
    start_state = 0
    accepting_states = []
    transitions = {}
    
    # Create a new start state
    new_start_state = STATE_COUNT
    increment_state_count()
    start_state = new_start_state

    # Add nfa_a and nfa_b's transitions
    for key in nfa_a.transitions:
        transitions[key] = nfa_a.transitions[key]
    for key in nfa_b.transitions:
        transitions[key] = nfa_b.transitions[key]

    # Add e (epsilon) transitions from new start state to nfa_a and nfa_b's start states
    transitions[start_state] = {'e': {nfa_a.start_state, nfa_b.start_state}}

    # Add nfa_a and nfa_b's accepting states
    for state in nfa_a.accepting_states:
        accepting_states.append(state)
    for state in nfa_b.accepting_states:
        accepting_states.append(state)

    return NFA(start_state, accepting_states, transitions)





"""
    ARGS:
    1: nfa_a - An NFA object to be operated on
    2: nfa_b - An NFA object to be operated on

    DESCRIPTION: Creates and returns a new NFA from the concatenation of nfa_a and nfa_b.
"""
def concat(nfa_a, nfa_b):
    start_state = 0
    accepting_states = []
    transitions = {}

    start_state = nfa_a.start_state

    # Add transitions from nfa_a and nfa_b
    for key in nfa_a.transitions:
        transitions[key] = nfa_a.transitions[key]
    for key in nfa_b.transitions:
        transitions[key] = nfa_b.transitions[key]

    # Take accepting states from nfa_a and create e (epsilon) transitions to start state of nfa_b
    for state in nfa_a.accepting_states:
        if state in transitions:
            transitions[state]['e'].add(nfa_b.start_state)
        else:
            transitions[state] = {'e': {nfa_b.start_state}}
    
    # Make accepting_states the accepting states from nfa_b
    accepting_states = nfa_b.accepting_states.copy()

    return NFA(start_state, accepting_states, transitions)





"""
    ARGS:
    1: nfa - An NFA object to be operated on

    DESCRIPTION: Creates and returns a new NFA from the kleene star of nfa.
"""
def kleene_star(nfa):
    start_state = 0
    accepting_states = []
    transitions = {}

    # Create a new start state
    new_start_state = STATE_COUNT
    increment_state_count()
    start_state = new_start_state

    # Add transitions from nfa
    for key in nfa.transitions:
        transitions[key] = nfa.transitions[key]

    # Add e (epsilon) transition from new start state to previous start state
    transitions[start_state] = {'e': {nfa.start_state}}

    # Add epsilon transitions from previous accepting states to new start state
    for state in nfa.accepting_states:
        transitions[state] = {'e': {start_state}}

    # Keep accepting states from previous nfa and make new start state accepting
    accepting_states = nfa.accepting_states.copy()
    accepting_states.append(start_state)
    
    return NFA(start_state, accepting_states, transitions)





def main():
    nfa_1 = operand_NFA("[100]")
    nfa_2 = operand_NFA("[001]")

    union_nfa = union(nfa_1, nfa_2)
    kleene_nfa = kleene_star(union_nfa)

    print(kleene_nfa.start_state)
    print(kleene_nfa.accepting_states)
    print(kleene_nfa.transitions)

    nfa_3 = operand_NFA("[100]")
    concat_nfa = concat(kleene_nfa, nfa_3)

main()