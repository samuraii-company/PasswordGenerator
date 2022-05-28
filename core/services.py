from abc import ABC, abstractmethod
from .generator import create_password, PasswordCredentials


class IPassword(ABC):
    @abstractmethod
    def generate_password(self):
        """Generate password abstract method"""
        ...


class Password(IPassword):
    def __init__(self, count: int, symbols: bool, numbers: bool):
        self.count: int = count
        self.symbols: bool = symbols
        self.numbers: bool = numbers

    def generate_password(self):
        _password = create_password(
            PasswordCredentials(self.count, self.numbers, self.symbols)
        )
        return _password.generate()

    @classmethod
    def only_letters_password(cls, sym_count: int) -> "Password":
        """Create instance of only letters"""

        return cls(count=sym_count, symbols=False, numbers=False)

    @classmethod
    def letters_with_numbers(cls, sym_count: int) -> "Password":
        """Create instance with letters and numbers"""

        return cls(count=sym_count, symbols=False, numbers=True)

    @classmethod
    def full_symbols(cls, sym_count: int) -> "Password":
        """Create instance with full symbols combinations"""

        return cls(count=sym_count, symbols=True, numbers=True)
