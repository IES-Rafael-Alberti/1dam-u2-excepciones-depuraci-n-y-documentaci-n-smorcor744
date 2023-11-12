import pytest
from src.ejer2_3_3 import cuenta_atras

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (1, "1, 0"),
        (3, "3, 2, 1, 0"),
        (5, "5, 4, 3, 2, 1, 0"),
        (7, "7, 6, 5, 4, 3, 2, 1, 0"),
    ]
)
def test_cuenta_atras(input_n, expected):
    assert cuenta_atras(input_n) == expected