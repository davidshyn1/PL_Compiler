from lexical import scanner

def set_grammar(grammar_path):
    with open(grammar_path, 'r', encoding="utf-8") as g:
        grammar_txt = g.read()
    grammar_list = grammar_txt.strip().split(";\n")
    grammar = dict()
    for trans in grammar_list:
        key, value = trans.split("->")
        key = key.strip()
        grammar[key] = []
        value = value.replace("([a-z] | [A-Z])*", "[a-z]* | [A-Z]*") #last grammar distributive rule
        value = value.replace('"', '') #delete quotation mark
        value = value.replace('\n', '') #delete enter
        value = value.replace(' ', '') #delete space
        value = value.split("|") #split 'or'
        for val in value:
            val = val.split()
            if len(val):
                grammar[key].append(val)
            else:
                grammar[key].append([""])

    return grammar


if __name__ == "__main__":
    # open test file
    with open("lexical_check.txt", 'r') as test:
        code = test.read()

    # scanner : print tokens
    scan = scanner(code)
    scan.lexical()
    tokens = scan.tokens
    for token in tokens:
        print(token)
    print()

    grammar = set_grammar('./grammar.txt')
    print(grammar)
