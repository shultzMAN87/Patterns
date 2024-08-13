# интерфейс Target, который ожидает клиент.
class Target:
    def request(self):
        return "Target: Default behavior"


# cуществующий класс Adaptee, который имеет несовместимый интерфейс.
class Adaptee:
    def specific_request(self):
        return "Adaptee: Specific behavior"


# адаптер, который преобразует интерфейс Adaptee в интерфейс Target.
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()}"


def client_code(target: Target):
    print(target.request())

# Клиент может работать с Target напрямую.
target = Target()
client_code(target)

# Клиент может работать с Adaptee через Adapter.
adaptee = Adaptee()
adapter = Adapter(adaptee)
client_code(adapter)
