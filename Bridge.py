from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: float):
        pass


class WindowsRenderer(Renderer):
    def render_circle(self, radius: float):
        print(f"Рисуем круг радиусом {radius} в Windows.")


class LinuxRenderer(Renderer):
    def render_circle(self, radius: float):
        print(f"Рисуем круг радиусом {radius} в Linux.")


class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self._renderer = renderer

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor: float):
        pass


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self._radius = radius

    def draw(self):
        self._renderer.render_circle(self._radius)

    def resize(self, factor: float):
        self._radius *= factor


# Пример использования
if __name__ == "__main__":
    # Создаем реализации для Windows и Linux
    windows_renderer = WindowsRenderer()
    linux_renderer = LinuxRenderer()

    # Создаем круги с разными реализациями
    circle_on_windows = Circle(windows_renderer, 5)
    circle_on_linux = Circle(linux_renderer, 10)

    # Рисуем круги
    circle_on_windows.draw()
    circle_on_linux.draw()

    # Изменяем размер и перерисовываем
    circle_on_windows.resize(2)
    circle_on_windows.draw()