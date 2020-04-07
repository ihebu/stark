import random
import secrets
import string

from .constants import DEFAULT_LENGTH, DEFAULT_TYPE
from .constants import TYPES


def shuffle(s):
    """Return a randomly shuffled version of string s."""
    s = list(s)
    random.shuffle(s)
    return "".join(s)


def pick(s, n):
    """Return a string with n randomly picked characters from string s."""
    return "".join(secrets.choice(s) for i in range(n))


def random_partition(keys, p):
    """Return a dict with keys such that values are a random partition of p.

    Parameters
    ----------
    keys : list of str
    p : int

    Returns
    -------
    result : dict
        keys : str
        values : int

    Notes
    -----
    each value of the dict should be greater than or equal 1

    Example
    -------
    >>> partition(['alphanumeric','hexdigits','symbols'],7)
    {'alphanumeric': 1, 'hexdigits': 2, 'symbols': 4}
    """
    n = len(keys)
    # Each key should at least have one character
    values = [1] * n
    p -= n
    for _ in range(p):
        i = secrets.randbelow(n)
        values[i] += 1
    result = {keys[i]: values[i] for i in range(n)}
    return result


def sumValues(d):
    """Return the sum of int values of a dict d."""
    result = 0
    for value in d.values():
        if type(value) == int:
            result += value
    return result


class Password:
    def __init__(self, length, args):
        self.args = dict(args)
        # If the password length is not privded
        # It will have the value of self.sum
        self.length = length or self.sum
        # Default password settings
        self.default_type = DEFAULT_TYPE
        self.default_length = self.length or DEFAULT_LENGTH
        self.type = TYPES

    @property
    def is_default(self):
        # If no args are specified the password will be default
        return self.args == dict()

    @property
    def sum(self):
        """Return the sum each type's length.

        Example : stark -l 10 -u 5 -d 7 --> self.sum = 10 + 5 + 7 = 22
        """
        return sumValues(self.args)

    @property
    def rest(self):
        return self.length - self.sum

    @property
    def empty(self):
        return [key for key, value in self.args.items() if type(value) != int]

    def create_map(self):
        """Create a map for the password.

        A map is dict with keys the types of characters and values the corresponding length
        Example : {'lowercase' : 15, 'digits' : 10, 'symbols' : 5}
        if the password length is not provided and no options are provided generate a password with default settings.
        if the password length is provided while the sum of the each type's length is less than the password length, complete the rest with default characters.
        if the length of each type is provided, the password length is optional.
        """
        if self.is_default:
            self.args = {self.default_type: self.default_length}
        else:
            if self.empty == []:
                self.args[self.default_type] = self.rest
            else:
                partition = random_partition(self.empty, self.rest)
                # Merge the partition with self.args
                self.args.update(partition)

        self.map = {self.type[key]: value for key, value in self.args.items()}

    def generate(self):
        """Generate a random password from a map."""
        self.create_map()
        result = ""
        for key, value in self.map.items():
            result += pick(key, value)
        return shuffle(result)
