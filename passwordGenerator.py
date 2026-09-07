import string
from random import choice

LOWER = tuple(string.ascii_lowercase)
UPPER = tuple(string.ascii_uppercase)
SPECIAL = tuple(string.punctuation)
NUMBERS = tuple(string.digits)

class Password:
    """Creates a password allowing for different character sets and lengths"""

    def __init__(self, has_lower, has_upper, has_special, has_numbers, _len):
        """Instantiation of variables used to determine password"""

        self.has_lower = has_lower
        self.has_upper = has_upper
        self.has_special = has_special
        self.has_numbers = has_numbers
        self._len = _len

        self.password = ""
        self.sets = []

        self.create_set()
        self.build()

    def get(self):
        return self.password

    def get_charset(self):
        """Get the list of character sets"""
        return self.sets

    def build(self):
        """Build the password based on its length"""
        for x in range(self._len):
            char_set = choice(self.sets)
            self.password += choice(char_set)

    def create_set(self):
        """Create a set based on"""
        if self.has_upper:
            self.sets.append(UPPER)

        if self.has_lower:
            self.sets.append(LOWER)

        if self.has_numbers:
            self.sets.append(NUMBERS)

        if self.has_special:
            self.sets.append(SPECIAL)

if __name__ == "__main__":
    print(__name__)