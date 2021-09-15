# https://sly.readthedocs.io/en/latest/sly.html

from sly import Lexer, Parser

class MPLLexer(Lexer):
    # Choose things to ignore
    ignore = ' \t'
    ignore_comment = r'\#.*'

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

    literals = {':', '(', ')', ',', '='}

    # Tokens
    tokens = {
        MIX,
        NAME,
        EQUALS,
        INTEGER,
        STRING
    }

    MIX = r'mix'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    EQUALS = r'==''
    @_(r'\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t
    STRING = r'\"[^"]\"'

class MPLParser(Parser):
    tokens = MPLLexer.tokens
    def __init__(self):
        self.names = {}

    @_('NAME "=" expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr

    @_('NAME')
    def expr(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print(f"Undefined name {p.NAME}")
            return 0

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('"(" INTEGER "," INTEGER "," INTEGER ")"')
    def color(self, p):
        # (R, G, B)
        return ( p.expr0, p.expr1, p.expr2 )

    @_('MIX ":" color color')
    def color(self, p):
        # Mix of the colors.
        return (
            int(0.5 * (p[2][0] p[3][0])),
            int(0.5 * (p[2][1] p[3][1])),
            int(0.5 * (p[2][2] p[3][2]))
        )

if __name__ == '__main__':
    lexer = MPLLexer()
    parser = MPLParser()
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
