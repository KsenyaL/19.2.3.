import pytest
from app.calculator import Calculator


class Test_Calculator:
    def setup(self):
        self.calculator = Calculator

    def test_multiply(self):
        assert self.calculator.multiply(self, 2, 4) == 8

    def test_division(self):
        assert self.calculator.division(self, 6, 3) == 2

    def test_subtraction(self):
        assert self.calculator.subtraction(self, 5, 2) == 3

    def test_adding(self):
        assert self.calculator.adding(self, 4, 3) == 7
