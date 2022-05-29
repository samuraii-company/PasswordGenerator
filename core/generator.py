from abc import ABC, abstractmethod
from typing import NamedTuple
import string
import random


SYMBOLS = "@!_[]:;*^%#"


class PasswordCredentials(NamedTuple):
    symbols_count: int
    digits: bool
    symbols: bool


class Generator(ABC):
    @abstractmethod
    def generate(self) -> str:
        """Generate password with included credentials"""
        ...


class PasswordGenerator(Generator):
    """Password Generator object"""

    def __init__(self, symbols_count: int):
        self.symbols_count = symbols_count
        self.letters = string.ascii_letters
        self.password = ""

    def generate(self) -> str:
        """Generate password"""

        for _ in range(self.symbols_count):
            self.password += random.choice(self.letters)

        return self.password


class LettersPasswordGenerator(PasswordGenerator):
    """Password Generator with only letters"""

    def __init__(self, symbols_count: int):
        super().__init__(symbols_count)


class NumbersPasswordGenerator(PasswordGenerator):
    """Password Generator with letters, numbers"""

    def __init__(self, symbols_count: int):
        super().__init__(symbols_count)
        self.letters = string.ascii_letters + string.digits


class SymbolsPasswordGenerator(PasswordGenerator):
    """Password Generator with letters, symbols"""

    def __init__(self, symbols_count: int):
        super().__init__(symbols_count)
        self.letters = string.ascii_letters + SYMBOLS


class FullComboPasswordGenerator(PasswordGenerator):
    """Password Generator with letters, numbers, symbols"""

    def __init__(self, symbols_count: int):
        super().__init__(symbols_count)
        self.letters = string.ascii_letters + string.digits + SYMBOLS


def create_password(credentials: PasswordCredentials) -> "Generator":
    """Creating password based on credentials"""

    if not credentials.digits and not credentials.symbols:
        return LettersPasswordGenerator(credentials.symbols_count)

    elif credentials.digits and not credentials.symbols:
        return NumbersPasswordGenerator(credentials.symbols_count)

    elif not credentials.digits and credentials.symbols:
        return SymbolsPasswordGenerator(credentials.symbols_count)

    else:
        return FullComboPasswordGenerator(credentials.symbols_count)
