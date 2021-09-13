from sly import Lexer, Parser

class MPLLexer(Lexer):
    tokens = {MIX, NAME, INTEGER}
    ignore = ' \t'
    literals = {':', '(', ')', ','}
    #DISPLAY = r"DISPLAY"
    MIX = r'mix'
    # Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

class MPLParser(Parser):
    tokens = MPLLexer.tokens
    precedence = (
        ("")
    )
    #print(tokens)
    def __init__(self):
        pass

    @_('"(" expr "," expr "," expr ")"')
    def value(self, p):
        return ( p.expr0, p.expr1, p.expr2 )

    @_('MIX ":" COLOR')
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
