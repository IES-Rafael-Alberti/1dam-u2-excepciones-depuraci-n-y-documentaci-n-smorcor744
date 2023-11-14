import pytest
from src.ejer2_4 import atgoritmo_burbuja

@pytest.mark.parametrize(
    "expected",
    [
        ([1, 3, 8, 14, 19]),
    ]
)
def test_atgoritmo_burbuja(expected):
    assert atgoritmo_burbuja(expected) == expected