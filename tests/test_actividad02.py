import pytest
from src.actividad02 import temp

@pytest.mark.parametrize(
    "input_temperatura, expected",
    [
        (100, 37.77777777777778),
        (7.5623, -13.576500000000001),
        (45, 7.222222222222222),
        ("fieo", )
    ]
)
def test_temp_params(input_temperatura, expected):
    assert temp(input_temperatura) == expected


def test_dividir_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        temp(1200.456, 0)

