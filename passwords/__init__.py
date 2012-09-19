import bcrypt

def hash(password, algorithm="bcrypt", cost=12):
    """ 
    Hash a password with a built-in salt using bcrypt
    """
    salt = bcrypt.gensalt(cost);
    return bcrypt.hashpw(password, salt)
    
def verify(password, hash):
    """
    Verify a password against a passed hash
    """
    salt = hash[:29]
    return bcrypt.hashpw(password, salt) == hash
    