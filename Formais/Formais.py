import sys
from RegularGrammar import RegularGrammar, Production

def main():
    gramatica = "S1 -> aA | aB | aC | bB | bC | cC | a | b | c | & A -> aA | aB | aC | a B -> bB | bC | b C -> cC | c"
    regular_grammar = RegularGrammar(gramatica)
    delta = regular_grammar.to_automaton()
    print(delta)

if __name__ == "__main__":
    sys.exit(int(main() or 0))
