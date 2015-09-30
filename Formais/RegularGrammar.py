class RegularGrammar():

    def __init__(self, non_terminals, terminals, productions, inicial_simbol):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions
        self.inicial_simbol = inicial_simbol
    
    def to_automaton(self):
        states = self.non_terminals
        states.add('accept')
        delta = dict()
        temp = dict()

        for production in self.productions:
            for _beta in production.beta:
                if _beta[0] in temp:
                    if len(_beta) == 2:
                        temp[_beta[0]].append(_beta[1])
                    else:
                        temp[_beta[0]].append('accept')
                else:
                    if len(_beta) == 2:
                        temp[_beta[0]] = [_beta[1]]
                    else:
                        temp[_beta[0]] = ['accept']
            delta[production.alfa] = temp
            temp = dict()

        return delta

class Production():

    def __init__(self, _alfa, _beta):
        self.alfa = _alfa
        self.beta = _beta