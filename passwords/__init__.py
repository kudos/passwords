__title__ = 'passwords'
__version__ = '0.1.0'

import pbkdf2
import os
import base64
from itertools import izip


try:
    import bcrypt
except ImportError:
    pass


def hash(password, algorithm="pbkdf2", cost=8):
    """
    Hash a password

    pbkdf2 sample:
        $pbkdf2-256-1$8$FRakfnkgpMjnqs1Xxgjiwgycdf68be9b06451039cc\
        0f7075ec1c369fa36f055b1705ec7a
    bcrypt sample:
        $bcrypt-2a$08$9y1RbQ8Acdxq72Scf2ZqwuFSk9leg7Y.7E/lyYrDEjtN6kTIG4GKi

    The returned strings are broken down into
        - The algorithm and version used
        - The cost factor, number of iterations over the hash
        - The salt
        - The password
    """
    if algorithm == "bcrypt":
        salt = bcrypt.gensalt(cost)
        return bcrypt.hashpw(password, salt).replace("$2a$", "$bcrypt-2a$")

    elif algorithm == "pbkdf2":
        meta, salt = _generate_salt(cost)

        for iteration in range(0, min(max(cost, 4), 31)):
            password = pbkdf2.pbkdf2_hex(password, salt)

        return meta + salt + password


def verify(password, hash):
    """
    Verify a password against a passed hash
    """
    head, algorithm, cost, salthash = hash.split("$")

    if algorithm == "pbkdf2-256-1":

        salt = salthash[:24]

        password_hash = salthash[24:]

        rehash = password

        for iteration in range(0, min(max(int(cost), 4), 31)):
            rehash = pbkdf2.pbkdf2_hex(rehash, salt)

        return _safe_str_cmp(rehash, password_hash)

    elif algorithm == "bcrypt-2a":
        # replace our algo identifier with bcrypt's internal one
        # for some reason bcrypt couples the algo information with
        # the salt rather than the completed hash
        hash = hash.replace("$bcrypt-2a$", "$2a$")
        salt = hash[:29]
        return _safe_str_cmp(bcrypt.hashpw(password, salt), hash)


def _safe_str_cmp(a, b):
    """
    Regular string compare will bail at the earliest opportunity
    which allows timing attacks

    Efficiently iterate over the hashes
    """
    if len(a) != len(b):
        return False
    rv = 0
    for x, y in izip(a, b):
        rv |= ord(x) ^ ord(y)
    return rv == 0


def _generate_salt(cost):
    meta = "$pbkdf2-256-1$" + str(cost) + "$"
    # using 18 instead of bcrypt's 16 because base64 is going to pad it anyway
    return meta, base64.b64encode(os.urandom(18))
