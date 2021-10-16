import jwt
from itsdangerous import TimedJSONWebSignatureSerializer


class Singer:
    """
    :param secret: str
    :param salt: str
    """
    def __init__(self, secret: str, salt: str):
        self._secret = secret
        self._salt = salt

    def pyjwt_encode(self, payload, expiration=20):
        token = jwt.encode(payload, self._secret, algorithm="HS256")
        return token.decode("utf-8")

    def pyjwt_decode(self, token):
        payload = jwt.decode(token, self._secret, algorithm="HS256")
        return payload

    def its_encode(self, payload, expiration=3600):
        s = TimedJSONWebSignatureSerializer(
            secret_key=self._secret,
            salt=self._salt,
            expires_in=expiration,
            algorithm_name="HS256"
        )
        token = s.dumps(payload, salt=self._salt).decode("utf-8")
        return token

    def its_decode(self, string):
        s = TimedJSONWebSignatureSerializer(
            secret_key=self._secret,
            salt=self._salt,
            algorithm_name="HS256",
        )
        payload = s.loads(string, salt=self._salt)
        return payload
