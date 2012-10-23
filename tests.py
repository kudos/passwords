from passwords import hash, verify


def test_pbkdf2_valid():
    hashed = hash('test1')
    assert verify('test1', hashed)


def test_pbkdf2_invalid():
    hashed = hash('test1')
    assert not verify('test2', hashed)


def test_bcrypt_valid():
    hashed = hash('test1', "bcrypt", 12)
    assert verify('test1', hashed)


def test_bcrypt_invalid():
    hashed = hash('test1', "bcrypt", 12)
    assert not verify('test2', hashed)
