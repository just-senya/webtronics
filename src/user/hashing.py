from passlib.context import CryptContext

password_ctx = CryptContext(schemes=["bcrypt"], deprecated='auto')

class Hasher():
    def bcrypt(password: str) -> str:
        return password_ctx.hash(password)
    
    def verify_password(hashed_password: str, password: str) -> bool:
        return password_ctx.verify(hashed_password, password)