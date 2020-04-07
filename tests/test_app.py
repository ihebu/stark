import pytest

from stark.app import generate
from stark.constants import TYPES


def is_derived(password, original):
    """Check if all characters of password are in original string."""
    n = len(password)
    for i in range(n):
        if password[i] not in original:
            return False
    return True


@pytest.mark.parametrize("characters", TYPES.keys())
def test_generate(characters):
    types = {characters: 20}
    password = generate(types=types)
    assert is_derived(password, TYPES[characters])
