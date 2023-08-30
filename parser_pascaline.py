from tokens_pascaline import TOKENS
from lexer_pascaline import Lexer

class Parser:
    def __init__(self, source) -> None:
        self.lexer = Lexer(source)
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Parsing error: invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token

        if token.type == TOKENS.INTEGER.name:
            self.eat(TOKENS.INTEGER.name)
            return token.value
        
        elif token.type == TOKENS.LPAREN.name:
            self.eat(TOKENS.LPAREN.name)
            result = self.expr()
            self.eat(TOKENS.RPAREN.name)
            return result
    
    def term(self):
        result = self.factor()

        while self.current_token.type in (TOKENS.MUL.name, TOKENS.DIV.name):
            token = self.current_token

            if token.type == TOKENS.MUL.name:
                self.eat(TOKENS.MUL.name)
                result = result * self.factor()
            elif token.type == TOKENS.DIV.name:
                self.eat(TOKENS.DIV.name)
                result = result / self.factor()

        return result

    def expr(self):
        result = self.term()

        while self.current_token.type in (TOKENS.PLUS.name, TOKENS.MINUS.name):
            token = self.current_token

            if token.type == TOKENS.PLUS.name:
                self.eat(TOKENS.PLUS.name)
                result = result + self.term()
            elif token.type == TOKENS.MINUS.name:
                self.eat(TOKENS.MINUS.name)
                result = result - self.term()

        return result
