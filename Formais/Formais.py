import sys

from regular_grammar import regular_grammar
from regular_sets.finite_automaton import DFA

def main():
    gramatica = "S1 -> aA | aB | aC | bB | bC | cC | a | b | c | & "\
                 "A -> aA | aB | aC | a "\
                 "B -> bB | bC | b "\
                 "C -> cC | c"
    regular_grammar = RegularGrammar(gramatica)
    delta = regular_grammar.to_automata()
    #print(delta)
    dfa = DFA(delta, 'S1', ['qAccept'])
    regular = dfa.to_grammar()
    #print(regular)

if __name__ == "__main__":
    sys.exit(int(main() or 0))
