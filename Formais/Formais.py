import sys
from RegularGrammar import RegularGrammar, Production

def make_it_proper_to_grammar(x):
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

    return RegularGrammar(non_terminals, terminals, list_of_productions, inicial_simbol)

def main():
    gramatica = "S1 -> aA | aB | aC | bB | bC | cC | a | b | c | & A -> aA | aB | aC | a B -> bB | bC | b C -> cC | c"
    regular_grammar = make_it_proper_to_grammar(gramatica)
    delta = regular_grammar.to_automaton()
    print(delta)

if __name__ == "__main__":
    sys.exit(int(main() or 0))

