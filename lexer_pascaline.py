from tokens_pascaline import Token, TOKENS

class Lexer:
    def __init__(self, source: str) -> None:
        self.source: str = source
        self.pos: int = 0
        self.current_char: str = self.source[self.pos]

    def error(self):
        raise Exception('Lexical error: invalid character')

    def advance(self):
        self.pos += 1

        if self.pos > len(self.source) - 1:
            self.current_char = None 
        else:
            self.current_char = self.source[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''

        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
            
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit():
                return Token(TOKENS.INTEGER.name, self.integer())
            
            match self.current_char:
                case '+':
                    self.advance()
                    return Token(TOKENS.PLUS.name, '+')
                case '-':
                    self.advance()
                    return Token(TOKENS.MINUS.name, '-')
                case '*':
                    self.advance()
                    return Token(TOKENS.MUL.name, '*')
                case '/':
                    self.advance()
                    return Token(TOKENS.DIV.name, '/')
                case '(':
                    self.advance()
                    return Token(TOKENS.LPAREN.name, '(')
                case ')':
                    self.advance()
                    return Token(TOKENS.RPAREN.name, ')')
            
            self.error()

        return Token(TOKENS.EOF.name, None)
