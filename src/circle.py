from src.figure import Figure

class Circle(Figure):
    PI = 3.141592653589793  # можно упростить до 3.14, но точность ниже

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Circle radius must be positive")
        self.radius = radius

    def get_area(self) -> float:
        return self.PI * (self.radius ** 2)

    def get_perimeter(self) -> float:
        return 2 * self.PI * self.radius


c = Circle(2)

print("CIRCLE")
print("radius:", c.radius)
print("area:", c.get_area())
print("perimeter:", c.get_perimeter())