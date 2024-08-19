from abc import ABC, abstractmethod


# Интерфейс посредника
class Mediator(ABC):
    @abstractmethod
    def send_message(self, message: str, colleague: 'Colleague'):
        pass


# Коллега (пользователь в чате)
class Colleague(ABC):
    def __init__(self, name: str, mediator: Mediator):
        self.name = name
        self.mediator = mediator

    @abstractmethod
    def receive(self, message: str):
        pass

    def send(self, message: str):
        print(f"{self.name} отправляет сообщение: {message}")
        self.mediator.send_message(message, self)


# Конкретный коллега
class User(Colleague):
    def receive(self, message: str):
        print(f"{self.name} получил сообщение: {message}")


# Конкретный посредник (чат)
class ChatRoom(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def send_message(self, message: str, sender: Colleague):
        for user in self.users:
            if user != sender:
                user.receive(message)

# Пример использования
if __name__ == "__main__":
    chat_room = ChatRoom()

    user1 = User("Alice", chat_room)
    user2 = User("Bob", chat_room)
    user3 = User("Charlie", chat_room)

    chat_room.add_user(user1)
    chat_room.add_user(user2)
    chat_room.add_user(user3)

    user1.send("Привет всем!")
    user2.send("Привет, Alice!")