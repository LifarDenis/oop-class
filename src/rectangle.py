#Прямоугольник

from src.figure import Figure                                    # импортируем базовый класс Figure
class Rectangle(Figure):                                         # объявляем класс Прямоугольник и наследуемся от Figure

    def __init__(self, side_a: int, side_b: int):                # конструктор: сюда приходят стороны a и b
        if side_a <= 0 or side_b <= 0:                           # простая валидация входных данных
            raise ValueError(f'Не может быть отрицательным {side_a},{side_b}') # если некорректно — бросаем ошибку

        super().__init__("Rectangle") # вызываем конструктор родителя и задаём имя фигуры
        self.side_a = side_a               # сохраняем сторону a в атрибут объекта
        self.side_b = side_b               # сохраняем сторону b в атрибут объекта

    @property                              # декоратор для свойства
    def area(self):                        # метод для вычисления площади
        return self.side_a * self.side_b   # формула площади прямоугольника: a * b

    @property                              # декоратор для свойства
    def perimeter(self):                   # метод для вычисления периметра
        return 2 * (self.side_a + self.side_b) # формула периметра: 2 * (a + b)


# --- пример использования (ниже уже не описание класса, а «скрипт») ---

r = Rectangle(3, 4) # создаём объект прямоугольника со сторонами 3 и 4
print(r.name)        # печатаем имя фигуры (поле пришло из Figure) -> "Rectangle"
print(r.area)     # вызываем метод площади -> 12
print(r.perimeter) # вызываем метод периметра -> 14





