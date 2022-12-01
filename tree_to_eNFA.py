# Global variable to keep track of how many states are created in the building process
STATE_COUNT = 0

def increment_state_count():
    global STATE_COUNT
    STATE_COUNT += 1

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
    