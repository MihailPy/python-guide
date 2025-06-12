import pytest
from src.utils import multiply, divide


class TestUtils:
    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(-1, 5) == -5

    def test_divide(self):
        assert divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Делить на ноль нельзя!"):
            divide(10, 0)
