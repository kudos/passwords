from passwords import crypt, verify


def test_valid():
    hashed = crypt('password')
    assert verify('password', hashed)


def test_invalid():
    hashed = crypt('password')
    assert not verify('password2', hashed)
