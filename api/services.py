from core.generator import PasswordCredentials, create_password


def create(credentials: PasswordCredentials) -> str:
    """Start Core module create password"""

    _password = create_password(credentials)

    return _password.generate()
