import pytest
from src.ejer2_3_1 import pedirEdad


def test_pedirEdad_Error():
    with pytest.raises(ValueError):
        pedirEdad(12)