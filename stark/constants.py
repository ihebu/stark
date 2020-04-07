import string

DEFAULT_LENGTH = 25
DEFAULT_TYPE = "alphanum"
TYPES = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "digits": string.digits,
    "symbols": string.punctuation,
    "letters": string.ascii_letters,
    "alphanum": string.ascii_letters + string.digits,
    "hexdigits": string.hexdigits,
    "any": string.ascii_letters + string.digits + string.punctuation,
}
