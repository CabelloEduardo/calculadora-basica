from operaciones import suma, resta, multiplicacion, division
import pytest

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(10, 5) == 5

def test_multiplicacion():
    assert multiplicacion(3, 4) == 12

def test_division_normal():
    assert division(10, 2) == 5

def test_division_cero():
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        division(10, 0)
