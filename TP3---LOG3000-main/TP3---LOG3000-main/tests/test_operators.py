from operators import add, subtract, multiply, divide
import pytest

class TestAdd:
    """Tests pour la fonction add()"""

    """Addition de deux nombres positifs"""
    def test_add_positive_numbers(self):
        assert add(5, 3) == 8
        assert add(10, 20) == 30

    """Addition de deux nombres negatifs"""
    def test_add_negative_numbers(self):
        assert add(-5, -3) == -8
        assert add(-10, 5) == -5

    """Addition avec zéro"""
    def test_add_with_zero(self):
        assert add(0, 5) == 5
        assert add(10, 0) == 10
        assert add(0, 0) == 0

    """Addition de nombres décimaux"""
    def test_add_floats(self):
        assert add(5.5, 3.2) == pytest.approx(8.7)
        assert add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtract:
    """Tests pour la fonction subtract()"""

    """Soustraction de deux nombres positifs"""
    def test_subtract_positive_numbers(self):
        assert subtract(10, 3) == 7

    """Soustraction de deux nombres negatifs"""
    def test_subtract_negative_result(self):
        assert subtract(3, 10) == -7

    """Soustraction avec zero"""
    def test_subtract_with_zero(self):
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5

    """Soustraction de nombres décimaux"""
    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2


class TestMultiply:
    """Tests pour la fonction multiply()"""

    """Multplication de deux nombres positifs"""
    def test_multiply_positive_numbers(self):
        assert multiply(5, 3) == 15

    """Multiplication avec zero"""
    def test_multiply_with_zero(self):
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0

    """Multplication avec un"""
    def test_multiply_with_one(self):
        assert multiply(7, 1) == 7

    """Multplication avec des nombres négatifs"""
    def test_multiply_negative_numbers(self):
        assert multiply(-5, 3) == -15
        assert multiply(-4, -2) == 8

    """Multiplication de nombres décimaux"""
    def test_multiply_floats(self):
        assert multiply(2.5, 4) == pytest.approx(10.0)


class TestDivide:
    """Tests pour la fonction divide()"""

    """Division de deux nombres positifs"""
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5.0

    """Teste la division donnant un résultat décimal avec reste
        et vérifie que la fonction divide retourne une valeur approximative correcte.
       """
    def test_divide_with_remainder(self):
        assert divide(10, 3) == pytest.approx(3.333, rel=0.01)

    """Division de nombres décimaux"""
    def test_divide_floats(self):
        assert divide(7.5, 2.5) == pytest.approx(3.0)

    """Divison par zero"""
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    """Addition de deux nombres négatifs"""
    def test_divide_negative_numbers(self):
        assert divide(-10, 2) == -5.0
        assert divide(10, -3) == pytest.approx(-3.333, rel=0.01)

