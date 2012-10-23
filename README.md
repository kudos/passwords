Passwords
===

[![Build Status](https://secure.travis-ci.org/kudos/passwords.png?branch=master)](https://next.travis-ci.org/kudos/passwords)

What is it?
---
Passwords is a Python library with a standard and simple interface to cryptographic hashing functions for passwords. Currently it supports and defautls to [PBKDF2](http://en.wikipedia.org/wiki/PBKDF2) along with optional support for [bcrypt](http://en.wikipedia.org/wiki/Bcrypt).

The strings generated contain all the information to recreate the hash from the original password. The algorithm used, the cost factor, the salt and the resulting password hash.

Usage
---
    import passwords

    password = "god"

    password_hash = passwords.hash(password)
    # '$pbkdf2-256-1$8$ndzIsQl2gH4R46d7BCzkWA1K909904c2fe5c48ea1b0bf64caf35663987e871628c5cdbfb'
    passwords.verify(password, password_hash) # True