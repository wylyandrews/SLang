from sly import Lexer

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, PRINT }
    ignore = '\t '
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }
    
    # Define tokens as regular expressions
    # (stored as raw strings)
    NAME = r'[a-zA-Z_][a-zA-z0-9_]*'
    STRING = r'\".*?\"'

    NAME['if'] = IF
    NAME['print'] = PRINT

    # Number tokens
    @_(r'\d+')
    def NUMBER(self, t):
        #convert it into a python integer
        t.value = int(t.value)
        return t

    # Comment token
    @_(r'//.*')
    def COMMENT(self, t):
        pass
    
    # Newline token (used only for showing errors in new line)
    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')
    """
    @_(r'\(')
    def lparen(self, t):
        t.type = '{'      # Set token type to the expected literal
        self.nesting_level += 1
        return t

    @_(r'\)')
    def rparen(t):
        t.type = '}'      # Set token type to the expected literal
        self.nesting_level -=1
        return t
        """