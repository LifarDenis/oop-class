import pytest
from src.circle import Circle


def test_circle_area():
    c = Circle(2)
    assert c.area == 12.566370614359172

def test_circle_perimeter():
    c = Circle(2)
    assert c.perimeter == 12.566370614359172

