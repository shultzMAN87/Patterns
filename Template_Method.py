from abc import ABC, abstractmethod

# Абстрактный класс, задающий шаблонный метод
class CaffeineBeverage(ABC):
    # Шаблонный метод
    def prepare_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    # Общие шаги алгоритма
    def boil_water(self):
        print("Кипячение воды")

    def pour_in_cup(self):
        print("Наливание в чашку")

    # Шаги, которые должны быть реализованы в подклассах
    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

# Конкретный класс для приготовления кофе
class Coffee(CaffeineBeverage):
    def brew(self):
        print("Заваривание кофе")

    def add_condiments(self):
        print("Добавление сахара и молока")

# Конкретный класс для приготовления чая
class Tea(CaffeineBeverage):
    def brew(self):
        print("Заваривание чая")

    def add_condiments(self):
        print("Добавление лимона")

# Пример использования
if __name__ == "__main__":
    print("Приготовление кофе:")
    coffee = Coffee()
    coffee.prepare_beverage()

    print("\nПриготовление чая:")
    tea = Tea()
    tea.prepare_beverage()