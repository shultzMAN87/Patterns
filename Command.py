from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class CopyCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.copy()

    def undo(self):
        print("Undoing copy operation")


class PasteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.paste()

    def undo(self):
        print("Undoing paste operation")

class TextEditor:
    def copy(self):
        print("Text copied to clipboard")

    def paste(self):
        print("Text pasted from clipboard")

class CommandInvoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("No commands to undo")


if __name__ == "__main__":
    editor = TextEditor()

    copy_command = CopyCommand(editor)
    paste_command = PasteCommand(editor)

    invoker = CommandInvoker()

    invoker.execute_command(copy_command)
    invoker.execute_command(paste_command)
    invoker.undo_last_command()
    invoker.undo_last_command()
