Passwords
===

[![Build Status](https://secure.travis-ci.org/kudos/passwords.png?branch=master)](https://next.travis-ci.org/kudos/passwords)

What is it?
---
Passwords is a Python library with a standard and simple interface to cryptographic hashing functions for passwords. It uses a bundled [PBKDF2](http://en.wikipedia.org/wiki/PBKDF2) to give it no external dependancies. Credit goes to Armin Ronacher for the algorithm [implementation](https://github.com/mitsuhiko/python-pbkdf2)

The strings generated contain all the information to recreate the hash from the original password. The algorithm used, the cost factor, the salt and the resulting password hash.

Why?
---
This is an attempt to make it easier for developers to find and use a cryptographic library suitable for password storage.

Usage
---
    import passwords

    password = "god"

    password_hash = passwords.crypt(password)
    # '$pbkdf2-256-1$8$ndzIsQl2gH4R46d7BCzkWA1K909904c2fe5c48ea1b0bf64caf35663987e871628c5cdbfb'
    passwords.verify(password, password_hash) # True