from Transition import *


class FA:
    def __init__(self):
        self.initial_state = ""
        self.states = []
        self.alphabet = []
        self.final_states = []
        self.transitions = []

    def reader(self, filename):
        file = open(filename, 'r')
        line = file.readline()

        # Denote with 'step' the current line we are in
        # if state is 1, it means we are reading the states, and so on
        step = 0

        while line != "":
            step += 1

            if step == 1:
                # read the sates
                line = line.split()
                self.states = line
                self.initial_state = self.states[0]

            elif step == 2:
                line = line.split()
                self.alphabet = line

            elif step == 3:
                line = line.split()
                self.final_states = line

            else:
                line = line.replace("->", " ")
                line = line.split()
                self.transitions.append(Transition(line[0], line[1], line[2]))

            line = file.readline()

    def is_deterministic(self):
        '''Checks if a finite automata is deterministic or not'''

        # check if a transition ever repeats itself
        checked_transitions = []
        for transition in self.transitions:
            state = transition.get_from_state()
            value = transition.get_value()
            pair = (state, value)

            if pair in checked_transitions:
                return False
            checked_transitions.append(pair)
        return True

    def get_state_transition(self, state):
        '''Returns the transition corresponding to a certain state'''
        for t in self.transitions:
            if t.get_from_state() == state:
                return t
        return None

    def get_next_state(self, state, value):
        '''Returns the transition from a state to another using a given value'''
        for t in self.transitions:
            if t.get_from_state() == state and t.get_value() == value:
                return t.get_to_state()
        return None

    def check_sequence(self, sequence):
        '''Takes a sequence as an input and verifies if it can be accepted or not'''
        current_state = self.get_initial_state()
        for s in sequence:
            if self.get_next_state(current_state, s) is not None:
                current_state = self.get_next_state(current_state, s)
            else:
                return False

        return True

    def get_states(self):
        return self.states

    def get_alphabet(self):
        return self.alphabet

    def get_initial_state(self):
        return self.initial_state

    def get_final_states(self):
        return self.final_states

    def get_transitions(self):
        return self.transitions
