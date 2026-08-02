from passlib.context import CryptContext


# Password hashing configuration.
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    """
    Converts a normal password into a secure hash.
    """
    return pwd_context.hash(password)



def verify_password(
    plain_password: str,
    hashed_password: str
):
    """
    Checks whether the entered password
    matches the stored hash.

    Returns:

    True  -> correct password
    False -> wrong password
    """

    return pwd_context.verify(
        plain_password,
        hashed_password
    )