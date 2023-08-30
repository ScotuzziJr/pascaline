from enum import Enum
from typing import Union

TOKENS = Enum("TOKENS", [
	"EOF",
	"INTEGER",
	"PLUS",
	"MINUS",
	"DIV",
	"MUL",
	"LPAREN",
	"RPAREN"
])

class Token:
	def __init__(self, type: str, value: Union[str, int]) -> None:
		self.type: str = type
		self.value: Union[str, int] = value

	def __repr__(self) -> str:
		return f"Token({self.type}, {self.value})"
