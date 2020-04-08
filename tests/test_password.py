import pytest

from stark.constants import DEFAULT_LENGTH, DEFAULT_TYPE, TYPES
from stark.password import Password


@pytest.mark.parametrize(
    "length, args, expected",
    [
        (None, {}, 0),
        (15, {}, 15),
        (15, {"lowercase": 10}, 15),
        (None, {"lowercase": 10, "uppercase": 10}, 20),
    ],
)
def test_length(length, args, expected):
    assert Password(length, args).length == expected


@pytest.mark.parametrize("length, args, expected", [(10, {}, 10), (None, {}, 25)])
def test_default_length(length, args, expected):
    assert Password(length, args).default_length == expected


@pytest.mark.parametrize(
    "length, args, expected",
    [
        (None, {"lowercase": 15, "uppercase": 6}, 21),
        (2, {"lowercase": 15, "uppercase": True}, 15),
        (None, {"lowercase": True, "uppercase": True}, 0),
    ],
)
def test_sum(length, args, expected):
    assert Password(length, args).sum == expected


@pytest.mark.parametrize(
    "length, args, expected",
    [
        (None, {}, True),
        (10, {}, True),
        (10, {"lowercase": 5}, False),
        (None, {"lowercase": 4, "digits": 15}, False),
    ],
)
def test_is_default(length, args, expected):
    assert Password(length, args).is_default == expected


@pytest.mark.parametrize(
    "length, args, expected",
    [
        (10, {}, 10),
        (None, {}, 0),
        (None, {"uppercase": 7}, 0),
    ],
)
def test_rest(length, args, expected):
    assert Password(length, args).rest == expected


@pytest.mark.parametrize(
    "length, args, expected",
    [
        (
            25,
            {"lowercase": 15, "uppercase": True, "digits": True},
            ["uppercase", "digits"],
        ),
        (25, {"hexdigits": 10, "uppercase": 5}, []),
    ],
)
def test_empty(length, args, expected):
    assert Password(length, args).empty == expected


@pytest.mark.parametrize(
    "length, args, expected",
    [
        (None, {}, {TYPES[DEFAULT_TYPE]: DEFAULT_LENGTH}),
        (30, {}, {TYPES[DEFAULT_TYPE]: 30}),
        (None, {"lowercase": 15}, {TYPES["lowercase"]: 15, TYPES[DEFAULT_TYPE]: 0}),
        (15, {"lowercase": 15}, {TYPES["lowercase"]: 15, TYPES[DEFAULT_TYPE]: 0}),
        (20, {"lowercase": 15}, {TYPES["lowercase"]: 15, TYPES[DEFAULT_TYPE]: 5}),
        (
            20,
            {"lowercase": 15, "uppercase": 4},
            {TYPES["lowercase"]: 15, TYPES["uppercase"]: 4, TYPES[DEFAULT_TYPE]: 1},
        ),
    ],
)
def test_create_map(length, args, expected):
    password = Password(length, args)
    password.create_map()
    assert password.map == expected


def test_create_map_partition():
    password = Password(30, {"lowercase": 15, "uppercase": True, "hexdigits": True})
    password.create_map()
    with pytest.raises(KeyError):
        password.map[password.type[password.default_type]]
    assert sum(password.map.values()) == 30
    assert password.map[password.type["lowercase"]] == 15
