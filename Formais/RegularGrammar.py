class RegularGrammar():
    
    def __init__(self, x):
        grammar = x.split(' ')
        inicial_simbol = grammar[0]
        non_terminals = set()
        terminals = set()
        list_of_productions = list()
        temporary_alfa = ''
        temporary_beta = list()

        grammar_length = len(grammar)

        for i in range(0, grammar_length):
            if grammar[i].isupper():            
                non_terminals.add(grammar[i])

            if not grammar[i] == '|' and not grammar[i] == '->' and not i == 0 and not grammar[i].isupper():
                temporary_beta.append(grammar[i])
                terminals.add(grammar[i][0])

            if grammar[i] == '->' or i == grammar_length - 1:
                if len(temporary_beta) > 0:
                    prod = Production(temporary_alfa, temporary_beta)
                    list_of_productions.append(prod)

                temporary_beta = list()
                temporary_alfa = grammar[i-1]

        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = list_of_productions
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