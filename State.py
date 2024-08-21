from abc import ABC, abstractmethod

# Интерфейс состояния
class TrafficLightState(ABC):
    @abstractmethod
    def change(self, context: 'TrafficLight'):
        pass

# Конкретные состояния
class RedLight(TrafficLightState):
    def change(self, context: 'TrafficLight'):
        print("Красный свет. Переключаемся на зеленый.")
        context.set_state(GreenLight())

class GreenLight(TrafficLightState):
    def change(self, context: 'TrafficLight'):
        print("Зеленый свет. Переключаемся на желтый.")
        context.set_state(YellowLight())

class YellowLight(TrafficLightState):
    def change(self, context: 'TrafficLight'):
        print("Желтый свет. Переключаемся на красный.")
        context.set_state(RedLight())

# Контекст
class TrafficLight:
    def __init__(self, state: TrafficLightState):
        self._state = state

    def set_state(self, state: TrafficLightState):
        self._state = state

    def change(self):
        self._state.change(self)

# Пример использования
if __name__ == "__main__":
    traffic_light = TrafficLight(RedLight())

    # Имитируем работу светофора
    traffic_light.change()  # Красный -> Зеленый
    traffic_light.change()  # Зеленый -> Желтый
    traffic_light.change()  # Желтый -> Красный
    traffic_light.change()  # Красный -> Зеленый