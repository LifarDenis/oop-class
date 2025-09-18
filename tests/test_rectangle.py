from src.rectangle import Rectangle
import pytest

def test_reactangle_area_perimeter():
    r = Rectangle(3, 4)
    assert r.area == 12
    assert r.perimeter == 14


def test_rectangle_validation_zero_or_negative():
    with pytest.raises(ValueError):
        Rectangle(0, 4)
    with pytest.raises(ValueError):
        Rectangle(-1, 5)


