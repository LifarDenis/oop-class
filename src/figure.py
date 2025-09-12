from __future__ import annotations
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def get_area(self) -> float:
        ...

    @abstractmethod
    def get_perimeter(self) -> float:
        ...

    def add_area(self, other: "Figure") -> float:
        if not isinstance(other, Figure):
            raise ValueError("Should be a Figure")
        return self.get_area() + other.get_area()

    # Удобные свойства (чтобы работали примеры из задания: square.area)
    @property
    def area(self) -> float:
        return self.get_area()

    @property
    def perimeter(self) -> float:
        return self.get_perimeter()
