import pytest
from src.ejer2_3_2 import numero_impar

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (1, "1"),
        (3, "1, 3"),
        (5, "1, 3, 5"),
        (7, "1, 3, 5, 7"),
        (9, "1, 3, 5, 7, 9"),
    ]
)
def test_numero_impar(input_n, expected):
    assert numero_impar(input_n) == expected