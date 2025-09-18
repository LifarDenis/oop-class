import pytest

from src.triagle import Triangle

def test_triagle_perimeter():
    t = Triangle(3, 4, 5)
    assert t.name == "Triangle"
    assert t.perimeter == 12

def test_triagle_area():
    t = Triangle(3, 4, 5)
    assert t.area == 6




