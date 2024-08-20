class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state


class TextEditor:
    def __init__(self):
        self._content = ""

    def type(self, text: str):
        self._content += text

    def save(self) -> Memento:
        return Memento(self._content)

    def restore(self, memento: Memento):
        self._content = memento.get_state()

    def get_content(self) -> str:
        return self._content


class History:
    def __init__(self):
        self._mementos = []

    def save(self, memento: Memento):
        self._mementos.append(memento)

    def undo(self) -> Memento:
        if not self._mementos:
            return None
        return self._mementos.pop()


if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.type("Hello, ")
    editor.type("world!")
    history.save(editor.save())

    editor.type(" How are you?")
    history.save(editor.save())

    editor.type(" I'm fine.")
    print(editor.get_content())  # Вывод: Hello, world! How are you? I'm fine.

    editor.restore(history.undo())
    print(editor.get_content())  # Вывод: Hello, world! How are you?

    editor.restore(history.undo())
    print(editor.get_content())  # Вывод: Hello, world!
