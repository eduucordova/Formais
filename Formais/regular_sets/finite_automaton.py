

class DFA:
    """Class that encapsulates a DFA."""

    def __init__(self, delta_transitions, initial_state, accept_states):
        self.delta = delta_transitions
        self.initial_state = initial_state
        self.accept_states = set(accept_states)

    def compute(self, state, input_string):
        """ compute strings in DFA
        :param state: is actual state
        :param input_string: string to compute
        :return: last state computed
        """
        state = {state}
        for a in input_string:
            state = self.delta[next(iter(state))][a]
        return next(iter(state))

    def validate_sentence(self, input_string):
        """
        :param input_string: sentence to validate
        :return: True, if is a valid sentence
                 False, otherwise
        """
        return self.compute(self.initial_state, input_string) in self.accept_states

    def to_grammar(self):
        productions = dict()
        temp = list()

        for state in self.delta:
            for transition in self.delta[state]:
                for next_state in self.delta[state][transition]:
                    if next_state in self.accept_states:
                        temp.append(transition)
                        temp.append(transition + next_state)
                    else:
                        temp.append(transition + next_state)
            productions[state] = temp
            temp = list()

        return productions