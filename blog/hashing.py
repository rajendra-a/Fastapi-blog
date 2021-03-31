from passlib.context import CryptContext


password_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return password_cxt.hash(password)

def verify(plainpassword, hashedpassword):
    return password_cxt.verify(plainpassword, hashedpassword)