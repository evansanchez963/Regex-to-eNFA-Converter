# Global variable to keep track of how many states are created in the building process
STATE_COUNT = 0

def increment_state_count():
    global STATE_COUNT
    STATE_COUNT += 1





"""
    This is an NFA class that stores the e-NFA and NFA of a given regex.
    Properties:
        1: states - A set of integers representing the states in the NFA
        2: alphabet - A set of operands plus epsilon representing the alphabet of the NFA
        3: start_state - An integer representing a starting state
        4: accepting_states - A set of integers that represent accepting states
        5: transitions - A dictionary of dictionaries where the key is an integer representing a state
        and the value is another dictionary. In those dictionaries, the key is a key in the alphabet
        and the value is a set of integers representing which states it transfers to.
        Example: {0: {'[000]': {0, 1}, '[111]': {0}}} means that starting from state 0, input [000] transitions
        to state 0 and state 1, and input [111] transitions to state 1.
"""
class NFA:
    def __init__(self, states=None, alphabet=None, start_state=None, accepting_states=None, transitions=None):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accepting_states = accepting_states
        self.transitions = transitions
    
    # Returns an epsilon enclosure (set of states reachable by epsilon only) for a given state
    def calc_e_closure(self, state):
        e_closure = set()
        stack = [state]

        while stack:
            curr_state = stack.pop()
            e_closure.add(curr_state)

            if "e" in self.transitions[curr_state].keys():
                next_states = self.transitions[curr_state]["e"]
                stack.extend(next_states)
                e_closure = e_closure.union(next_states)

        return e_closure
    
    # TODO: Create a function called remove_e_moves() that removes epsilon transitions from the NFA
    def remove_e_moves(self):
        #for state in self.transitions.keys():
        #    e_closure = self.calc_e_closure(state)
        #    print(f"State: {state}, e_closure: {e_closure}")
        new_state = set()
        new_alpha = set()
        new_transitions = {}
        new_accept = set()
        new_start = 0

        while(self.e_exists(self.transitions)):

            for state in self.transitions.keys():
                for key in self.transitions[state].keys():
                    if key == 'e':
                        newnew_transitions = {}
                        for i in self.transitions[state][key]:
                            for new_key in self.transitions[i].keys():
                                a = new_key
                                b = self.transitions[i][new_key]
                                #b = self.calc_e_closure(new_key)

                                if a in newnew_transitions.keys():
                                    newnew_transitions[a] = set.union(newnew_transitions[a], b)
                                else:
                                    newnew_transitions[a] = b

                        new_transitions[state] = newnew_transitions
                    else:
                        new_transitions[state] = self.transitions[state]

            self.transitions = new_transitions
            print(new_transitions)
            print()

        new_state = self.states
        new_alpha = self.alphabet
        new_alpha.remove("e")
        new_accept = self.accepting_states      # TODO: Update accepting states
        new_start = self.start_state

        return NFA(new_state, new_alpha, new_start, new_accept, new_transitions)
                        

    def e_exists(self, transitions):
        for i in transitions:
            for j in transitions[i]:
                if (j == "e"):
                    return True

        return False

                    

    # TODO: Create a function called accepts that determines if an alphabet array is accepted by the NFA or not
    def accepts(alphabet_arr):
        pass





"""
    ARGS:
    1: e_operand - A string "e" representing epsilon

    DESCRIPTION: Creates and returns an nfa for epsilon. The start state is the same as the accepting state.
"""
def epsilon_NFA():
    states = set()
    alphabet = set()
    start_state = 0
    accepting_states = set()
    transitions = {}

    start_state = STATE_COUNT
    increment_state_count()
    states.add(start_state)

    accepting_states.add(start_state)

    return NFA(states, alphabet, start_state, accepting_states, transitions)





"""
    ARGS:
    1: operand - An operand to be converted into an NFA, can be an alphabet ([000]-[999]) or e (epsilon)

    DESCRIPTION: Creates and returns an nfa for an operand. Creates a new start state and end state
    where the transition from the start state to the end state is the given operand.
"""
def operand_NFA(operand):
    states = set()
    alphabet = set()
    start_state = 0
    accepting_states = set()
    transitions = {}

    alphabet.add(operand)

    # Create a new start state
    start_state = STATE_COUNT
    increment_state_count()
    states.add(start_state)

    # Create a new accepting state
    new_accepting_state = STATE_COUNT
    increment_state_count()
    accepting_states.add(new_accepting_state)
    states.add(new_accepting_state)

    # Create a transition (operand) from start state to new accepting state
    transitions[start_state] = {operand: {new_accepting_state}}

    return NFA(states, alphabet, start_state, accepting_states, transitions)





"""
    ARGS:
    1: nfa_a - An NFA object to be operated on
    2: nfa_b - An NFA object to be operated on

    DESCRIPTION: Creates and returns a new NFA from the union of nfa_a and nfa_b.
"""
def union(nfa_a, nfa_b):
    states = set()
    alphabet = set()
    start_state = 0
    accepting_states = set()
    transitions = {}

    states = set.union(nfa_a.states, nfa_b.states)
    alphabet = set.union(nfa_a.alphabet, nfa_b.alphabet)
    
    # Create a new start state
    start_state = STATE_COUNT
    increment_state_count()
    states.add(start_state)

    # Add nfa_a and nfa_b's transitions
    for key in nfa_a.transitions:
        transitions[key] = nfa_a.transitions[key]
    for key in nfa_b.transitions:
        transitions[key] = nfa_b.transitions[key]

    # Add e (epsilon) transitions from new start state to nfa_a and nfa_b's start states
    transitions[start_state] = {'e': {nfa_a.start_state, nfa_b.start_state}}
    alphabet.add("e")

    # Add nfa_a and nfa_b's accepting states
    accepting_states = set().union(nfa_a.accepting_states, nfa_b.accepting_states)

    return NFA(states, alphabet, start_state, accepting_states, transitions)





"""
    ARGS:
    1: nfa_a - An NFA object to be operated on
    2: nfa_b - An NFA object to be operated on

    DESCRIPTION: Creates and returns a new NFA from the concatenation of nfa_a and nfa_b.
"""
def concat(nfa_a, nfa_b):
    states = set()
    alphabet = set()
    start_state = 0
    accepting_states = set()
    transitions = {}

    states = set.union(nfa_a.states, nfa_b.states)
    alphabet = set.union(nfa_a.alphabet, nfa_b.alphabet)
    start_state = nfa_a.start_state

    # Add transitions from nfa_a and nfa_b
    for key in nfa_a.transitions:
        transitions[key] = nfa_a.transitions[key]
    for key in nfa_b.transitions:
        transitions[key] = nfa_b.transitions[key]

    # Take accepting states from nfa_a and create e (epsilon) transitions to start state of nfa_b
    alphabet.add("e")
    for state in nfa_a.accepting_states:
        if state in transitions:
            transitions[state]['e'].add(nfa_b.start_state)
        else:
            transitions[state] = {'e': {nfa_b.start_state}}
    
    # Make accepting_states the accepting states from nfa_b
    accepting_states = nfa_b.accepting_states.copy()

    return NFA(states, alphabet, start_state, accepting_states, transitions)





"""
    ARGS:
    1: nfa - An NFA object to be operated on

    DESCRIPTION: Creates and returns a new NFA from the kleene star of nfa.
"""
def kleene_star(nfa):
    states = set()
    alphabet = set()
    start_state = 0
    accepting_states = set()
    transitions = {}

    states = nfa.states
    alphabet = nfa.alphabet

    # Create a new start state
    start_state = STATE_COUNT
    increment_state_count()
    states.add(start_state)

    # Add transitions from nfa
    for key in nfa.transitions:
        transitions[key] = nfa.transitions[key]

    # Add e (epsilon) transition from new start state to previous start state
    alphabet.add("e")
    transitions[start_state] = {'e': {nfa.start_state}}

    # Add epsilon transitions from previous accepting states to new start state
    for state in nfa.accepting_states:
        transitions[state] = {'e': {start_state}}

    # Keep accepting states from previous nfa and make new start state accepting
    accepting_states = nfa.accepting_states.copy()
    accepting_states.add(start_state)
    
    return NFA(states, alphabet, start_state, accepting_states, transitions)





"""
    ARGS:
    1: root - The root of the expression tree that is used to build the e-NFA

    DESCRIPTION: Creates and returns a new e-NFA. The e-NFA is recursively built using in-order traversal.
"""
def build_eNFA(root):
    # Base case
    if root is None:
        return None

    # Make NFAs for operands
    if root.left is None and root.right is None:
        if root.data == "e":
            return epsilon_NFA()    
        return operand_NFA(root.data)

    # Recursively build left tree
    left_NFA = build_eNFA(root.left)

    # Recursively build right tree
    right_NFA = build_eNFA(root.right)
    
    # Check and apply operation
    if root.data == "+":
        return union(left_NFA, right_NFA)
    elif root.data == ".":
        return concat(left_NFA, right_NFA)
    else:
        # Kleene star only has a left subtree and no right child
        return kleene_star(left_NFA)