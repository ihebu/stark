from .password import Password
from .validation import validate


def generate(length=None, types={}):
    """Generate a random password, given a length and types.

    Parameters
    ----------
    length: int or None
        the length of password

    types: dict
        the types of characters in the password and their length

        allowed keys:
            'lowercase'
            'uppercase'
            'digits'
            'symbols'
            'letters'
            'alphanumeric'
            'hexdigits'
            'any'

        allowed values:
            a positive int or True.

    Returns
    -------
    password: str
        The password with given length and parameters.

    Notes
    -----
    A value of True in types indicates that the character
    will have a number of one or more (randomly) in the password.
    If length is None, the password length
    will be the sum of the values of types.
    Thus, it's not allowed to have one value equals True
    while length is None.

    Examples
    --------
    >> from stark import generate
    >>
    >> types = {'lowercase':15,'digits':10,'symbols':True}
    >> generate(length=30,types=types)
    'o#41qc2i2t)e;t\\2f3a73qd11qwp+x'
    >>
    >> types = {'hexdigits':10,'digits':True }
    >> generate(length=15,types=types)
    '0eB87A724A0b235'
    >>
    >> types = {'uppercase':20,'digits':5 }
    >> generate(types=types)
    'A15UTI4NMPARITNLZFFB7IKX1'
    """

    validate(length, types)
    generator = Password(length, types)
    password = generator.generate()
    return password
