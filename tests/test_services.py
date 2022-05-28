from core.services import Password


class TestServices:
    def test_password_letters(self):

        password = Password.only_letters_password(20)

        _password = password.generate_password()

        assert len(_password) == 20

        assert type(_password) is str

    def test_pasword_numbers(self):

        password = Password.letters_with_numbers(20)

        _password = password.generate_password()

        assert len(_password) == 20

        assert type(_password) is str

    def test_pasword_symbols(self):

        password = Password.full_symbols(30)

        _password = password.generate_password()

        assert len(_password) == 30

        assert type(_password) is str
