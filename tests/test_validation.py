import pytest

from stark.validation import validate_length, validate_logic, validate_types


def test_validate_length():
    assert validate_length(None) == True
    assert validate_length(5) == True
    assert validate_length(1) == True
    with pytest.raises(TypeError):
        validate_length("5")
    with pytest.raises(ValueError):
        validate_length(-2)
    with pytest.raises(ValueError):
        validate_length(0)


def test_validate_types():
    with pytest.raises(TypeError):
        validate_types(2)
    with pytest.raises(TypeError):
        validate_types({"lowercase": "5"})
    with pytest.raises(ValueError):
        validate_types({"lowercase": False})
    with pytest.raises(ValueError):
        validate_types({"other": -2})
    assert validate_types({"uppercase": 5, "digits": 15}) == True
    assert validate_types({"uppercase": 5, "digits": True}) == True


def test_validate_logic():
    with pytest.raises(ValueError):
        validate_logic(15, {"lowercase": 15, "uppercase": True})
    with pytest.raises(ValueError):
        validate_logic(20, types={"lowercase": 15, "uppercase": 6})
    with pytest.raises(TypeError):
        validate_logic(None, {"lowercase": True})
        validate_logic(None, {"lowercase": 15, "symbols": True})
    assert validate_logic(20, {"lowercase": 15, "symbols": True})
    assert validate_logic(None, {"lowercase": 15, "symbols": 5})
