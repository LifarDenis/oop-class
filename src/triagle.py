#Треугольник
from src.figure import Figure  # импортируем базовый класс Figure

class Triangle(Figure):  # создаём класс Треугольник, наследуем от Figure
    def __init__(self, a: float, b: float, c: float):  # конструктор принимает 3 стороны
        if a <= 0 or b <= 0 or c <= 0:  # проверка: стороны должны быть положительные
            raise ValueError("Треугольник не может быть отрицательным")
        super().__init__("Triangle")  # вызываем конструктор родителя Figure
        self.name = "Triangle"        # задаём имя фигуры
        self.a = a  # сохраняем сторону a
        self.b = b  # сохраняем сторону b
        self.c = c  # сохраняем сторону c

    @property
    def perimeter(self):
        # периметр треугольника: a + b + c
        return self.a + self.b + self.c

    @property
    def area(self):
        # площадь по формуле Герона: √(p * (p - a) * (p - b) * (p - c))
        p = self.perimeter / 2  # полупериметр
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


# --- пример использования ---
t = Triangle(3, 4, 5)    # создаём треугольник со сторонами 3, 4, 5

print(t.name)       # "Triangle"
print(t.area)       # 6.0 (правильная площадь по Герону)
print(t.perimeter)  # 12 (сумма сторон)

