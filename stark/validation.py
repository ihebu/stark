def validate_length(length):
    """Check of if password length is valid.

    password length is valid if it's either None or a positif int
    """
    if length is None:
        return True
    if type(length) != int:
        raise TypeError("password length must be of type int")
    if length <= 0:
        raise ValueError("password length must be greater than or equal 1")
    return True


def validate_types(types):
    """Check if types is valid.

    types are is valid if it's of type dict
    keys should be a valid character type
    values should be either True or a positif int
    """
    if type(types) != dict:
        raise TypeError("types must be of type dict")
    allowed = [
        "lowercase",
        "uppercase",
        "digits",
        "symbols",
        "letters",
        "alphanumeric",
        "hexdigits",
        "any",
    ]
    for key in types.keys():
        if key not in allowed:
            raise ValueError("unknown character type : ", key)
    for value in types.values():
        if type(value) not in (int, bool):
            raise TypeError("value must be of type int or bool")
        if value == False or value <= 0:
            raise ValueError("invalud value specified")
    return True


def validate_logic(length, types):
    # check if the sum of the length of each type exceeds the password length
    if length and sum(types.values()) > length:
        raise ValueError("password length exceeded")
    # check if password length is not specified
    # and if there is a type with no specified length
    if not length and any(type(value) == bool for value in types.values()):
        raise TypeError("password length not specified")
    return True


def validate(length, types):
    validate_length(length)
    validate_types(types)
    validate_logic(length, types)
