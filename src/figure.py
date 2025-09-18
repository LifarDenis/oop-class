class Figure:  # базовый класс для всех фигур
    def __init__(self, name):
        self.name = name  # сохраняем имя фигуры (например, "Rectangle", "Circle")

    def area(self):
        # базовый метод площади, здесь он пустой
        # наследники ОБЯЗАНЫ его переопределить
        raise NotImplementedError("Метод area() должен быть реализован в наследнике")

    def perimeter(self):
        # базовый метод периметра, тоже только шаблон
        raise NotImplementedError("Метод perimeter() должен быть реализован в наследнике")

    def add_area(self, figure):
        # проверяем, что аргумент действительно является фигурой
        # У ТЕБЯ ошибка: сейчас написано if isinstance → raise
        # а надо наоборот: если НЕ фигура — ошибка
        if not isinstance(figure, Figure):
            raise ValueError("Аргумент должен быть экземпляром класса Figure")
        # возвращаем сумму площадей двух фигур
        return self.area() + figure.area()



