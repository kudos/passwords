__title__ = 'passwords'
__version__ = '0.1.0'


from os import urandom
from base64 import b64encode
from itertools import izip
import pbkdf2


def crypt(password, cost=2):
    """
    Hash a password

    result sample:
        $pbkdf2-256-1$8$FRakfnkgpMjnqs1Xxgjiwgycdf68be9b06451039cc\
        0f7075ec1c369fa36f055b1705ec7a

    The returned string is broken down into
        - The algorithm and version used
        - The cost factor, number of iterations over the hash
        - The salt
        - The password
    """

    salt = _generate_salt(cost)

    hashed = pbkdf2.pbkdf2_hex(password, salt, cost * 500)

    return "$pbkdf2-256-1$" + str(cost) + "$" + salt + "$" + hashed


def verify(password, hash):
    """
    Verify a password against a passed hash
    """
    _, algorithm, cost, salt, password_hash = hash.split("$")

    password = pbkdf2.pbkdf2_hex(password, salt, int(cost) * 500)

    return _safe_str_cmp(password, password_hash)


def _safe_str_cmp(a, b):
    """
    Internal function to efficiently iterate over the hashes
    
    Regular string compare will bail at the earliest opportunity
    which allows timing attacks
    """
    if len(a) != len(b):
        return False
    rv = 0
    for x, y in izip(a, b):
        rv |= ord(x) ^ ord(y)
    return rv == 0


def _generate_salt(cost):
    return b64encode(urandom(18))
