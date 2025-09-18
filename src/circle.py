#Круг
# Круг
from src.figure import Figure  # импортируем базовый класс Figure

class Circle(Figure):  # создаём класс Circle, наследуем от Figure
    def __init__(self, radius: float):  # конструктор принимает радиус
        if radius <= 0:  # проверка: радиус должен быть положительным
            raise ValueError('Радиус круга должен быть положительным числом')
        super().__init__("Circle")  # вызываем конструктор Figure, задаём имя "Circle"
        self.name = "Circle"        # сохраняем имя фигуры (избыточно, но можно оставить)
        self.radius = radius        # сохраняем радиус в атрибут объекта
        self.PI = 3.141592653589793 # константа π (без math)

    @property  # делаем метод как свойство (можно вызывать без скобок)
    def area(self):
        # площадь круга: π * r²
        return self.PI * (self.radius ** 2)

    @property
    def perimeter(self):
        # периметр (длина окружности): 2 * π * r
        return 2 * self.PI * self.radius


# --- пример использования ---
c = Circle(2)             # создаём круг с радиусом 2
print(c.name)             # "Circle"
print(c.area)             # 12.566370614359172 (π * 4)
print(c.perimeter)        # 12.566370614359172 (2 * π * 2)






