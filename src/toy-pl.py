from sly import Lexer, Parser

class MPLLexer(Lexer):
    tokens = {TALK, ANIMAL}
    ignore = ' \t'
    literals = {':'}
    #DISPLAY = r"DISPLAY"
    TALK = r'talk'
    # Tokens
    ANIMAL = r'[a-zA-Z_][a-zA-Z0-9_]*'
    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

class MPLParser(Parser):
    tokens = MPLLexer.tokens
    #print(tokens)
    def __init__(self):
        pass
    @_('TALK ":" ANIMAL')
    def value(self, p):
        #print(p[2])
        # Mix of the paints.
        if (p[2] == "cat"):
            print("Meow")
        elif (p[2] == "horse"):
            print("Neigh")

if __name__ == '__main__':
    lexer = MPLLexer()
    parser = MPLParser()
    #parser.parse(lexer.tokenize("talk : cat"))
    while True:
        try:
            text = input('Enter colors to mix > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            #for token in lex:
             #   print(token)
            parser.parse(lex)
    pass # remove pass to add your implementation ...