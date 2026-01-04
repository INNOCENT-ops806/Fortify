"""
A software to generate passwords randomly @author: Yahm3(https://github.com/Yahm3)
"""

import argparse  # module for command-line parsing
import re
import secrets
import string
import pyperclip

parser = argparse.ArgumentParser(description="generate a password")
parser.add_argument(dest="")


# Function to copy the generated password to the clipboard
def copy_to_the_clipboard(password_as_arg):
    pyperclip.copy(password_as_arg)


def generate(length=10, nums=1, special_chars=1, uppercase=1, lowercase=1):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_characters = letters + digits + symbols

    while True:
        password = ""
        for _ in range(length):
            password += secrets.choice(all_characters)
            constraints = [
                (nums, r"\d"),
                (special_chars, rf"[{symbols}]"),
                (uppercase, r"[A-Z]"),
                (lowercase, r"[a-z]"),
            ]

            if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
            ):
                break

        copy_to_the_clipboard(password)
        return password


if __name__ == "__main__":
    new_password = generate(
        length=8,
        special_chars=1,
        nums=1,
        uppercase=1,
        lowercase=1,
    )
    print(new_password)
