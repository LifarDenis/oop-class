
import pytest

from src.square import Square


def test_square():
    s = Square(5)
    assert s.area == 25


def test_perimeter():
    s = Square(5)
    assert s.perimeter == 20



