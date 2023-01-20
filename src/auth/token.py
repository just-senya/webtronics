from datetime import datetime, timedelta
from jose import JWTError, jwt
import sys

from . import schema

sys.path.append("/Users/arsen/Documents/programs/webtronics")
from config import config

SECRET_KEY = config.secret_key
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTE = 60


def create_access_token(data: dict):
    to_encode = dict(data)
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_token(token: str, exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        if not email:
            raise exception
        token_data = schema.TokenData(email=email)
    except JWTError:
        raise exception