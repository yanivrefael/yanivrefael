#test_addition.py
from src.calculator import add
import pytest
# tes1t
def test_add():
    result = add(3, 4)
    assert result == 7
def test_add_string():
    with pytest.raises(TypeError):
        add("stringa", 4)
