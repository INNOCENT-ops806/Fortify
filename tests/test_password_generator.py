import re
from src.password_generator import generate


def test_password_length():
    pw = generate(length=12)
    assert len(pw) == 12


def test_password_contains_digit():
    pw = generate(length=12, nums=1)
    assert re.search(r"\d", pw)


def test_password_contains_special_char():
    pw = generate(length=12, special_chars=1)
    assert re.search(r"[!\"#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~]", pw)


def test_password_contains_uppercase():
    pw = generate(length=12, uppercase=1)
    assert re.search(r"[A-Z]", pw)


def test_password_contains_lowercase():
    pw = generate(length=12, lowercase=1)
    assert re.search(r"[a-z]", pw)
