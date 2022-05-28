from core.generator import (
    LettersPasswordGenerator,
    NumbersPasswordGenerator,
    SymbolsPasswordGenerator,
)


class TestGenerator:
    def test_letter_password_generator(self):

        password = LettersPasswordGenerator(20)

        _password = password.generate()

        assert len(_password) == 20

        assert type(_password) is str

    def test_numbers_password_generator(self):

        password = NumbersPasswordGenerator(40)

        _password = password.generate()

        assert len(_password) == 40

        assert type(_password) is str

    def test_symbols_password_generator(self):

        password = SymbolsPasswordGenerator(50)

        _password = password.generate()

        assert len(_password) == 50

        assert type(_password) is str
