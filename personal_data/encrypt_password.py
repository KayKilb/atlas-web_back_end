#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Password hashing"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """function checks if a plaintext password matches a previously hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
