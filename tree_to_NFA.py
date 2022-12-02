# Global variable to keep track of how many states are created in the building process
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
        and the value is an integer representing which state in transfers to.
        Example: {0 (state): {'[000]': 0, '[111]':1}} means that starting from state 0, input [000] transitions
        to state 0 and input [111] transitions to state 1.
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
def create_operand_NFA(operand):
    start_state = ""
    accepting_states = []
    transitions = {}

    new_start_state = "q" + str(STATE_COUNT)
    