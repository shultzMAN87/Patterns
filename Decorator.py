from abc import ABC, abstractmethod


# Интерфейс компонента
class TextComponent(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


# Конкретный компонент
class SimpleText(TextComponent):
    def __init__(self, text: str):
        self._text = text

    def render(self) -> str:
        return self._text + '!!!'


# Абстрактный декоратор
class TextDecorator(TextComponent):
    def __init__(self, component: TextComponent):
        self._component = component

    def render(self) -> str:
        return self._component.render()


# Конкретный декоратор, добавляющий кавычки
class QuotedTextDecorator(TextDecorator):
    def render(self) -> str:
        return f'"{super().render()}"'


# Конкретный декоратор, добавляющий звездочки
class StarredTextDecorator(TextDecorator):
    def render(self) -> str:
        return f'*{super().render()}*'


# Конкретный декоратор, переводящий текст в верхний регистр
class UpperCaseTextDecorator(TextDecorator):
    def render(self) -> str:
        return super().render().upper()


if __name__ == "__main__":
    simple_text = SimpleText("Hello, World!")

    quoted_text = QuotedTextDecorator(simple_text)
    starred_text = StarredTextDecorator(quoted_text)
    uppercased_text = UpperCaseTextDecorator(starred_text)

    fully_decorated_text = UpperCaseTextDecorator(
        StarredTextDecorator(
            QuotedTextDecorator(simple_text)))

    print("Текст с кавычками:", quoted_text.render())
    print("Текст с кавычками и звездочками:", starred_text.render())
    print("Текст с кавычками, звездочками и верхним регистром:", uppercased_text.render())
    print("Тоже самое, но созданное одним вызовом:", fully_decorated_text.render())