import pytest

from stark.validation import validate_length, validate_logic, validate_types


@pytest.mark.parametrize(
    "length, expected",
    [
        (None,True),
        (5,True),
        (1,True)
    ]
)
def test_validate_length(length,expected):
    assert validate_length(length) == expected

@pytest.mark.parametrize(
    "length, expected",
    [
        ("5",TypeError),
        (-2,ValueError),
        (0,ValueError)
    ]
)
def test_validate_length_exceptions(length,expected):
    with pytest.raises(expected):
        validate_length(length)
    


@pytest.mark.parametrize(
    'types, expected',
    [
     ({"uppercase": 5, "digits": 15},True),
     ({"uppercase": 5, "digits": True},True)   
    ]
)
def test_validate_types(types,expected):
    assert validate_types(types) == expected

@pytest.mark.parametrize(
    'types, expected',
    [
     (2,TypeError),
     ({"lowercase": "5"},TypeError),
     ({"lowercase": False},ValueError),
     ({"other": -2},ValueError)   
    ]
)
def test_validate_types_exceptions(types,expected):
    with pytest.raises(expected):
        validate_types(types)

@pytest.mark.parametrize(
    'length, types, expected',
    [
        (20,{"lowercase": 15, "symbols": True},True),
        (None, {"lowercase": 15, "symbols": 5},True),
    ]
)
def test_validate_logic(length,types,expected):
    assert validate_logic(length, types) == expected


@pytest.mark.parametrize(
    'length, types, expected',
    [
        (15,{"lowercase": 15, "uppercase": True},ValueError),
        (20,{"lowercase": 15, "uppercase": 6},ValueError),
        (None,{"lowercase": True},TypeError),
        (None, {"lowercase": 15, "symbols": True},TypeError)
    ]
)
def test_validate_logic_exceptions(length,types,expected):
    with pytest.raises(expected):
        validate_logic(length, types)