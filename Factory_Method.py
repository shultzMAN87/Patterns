from abc import ABC, abstractmethod


class IProduct(ABC):
    @abstractmethod
    def release(self):
        pass


class Car(IProduct):
    def release(self):
        print('Light')


class Truck(IProduct):
    def release(self):
        print('Heavy')


class IWorkShop(ABC):
    @abstractmethod
    def create(self) -> IProduct:
        pass


class CarWorkShop(IWorkShop):
    def create(self) -> IProduct:
        return Car()


class TruckWorkShop(IWorkShop):
    def create(self) -> IProduct:
        return Truck()


if __name__ == "__main__":
    creator = CarWorkShop()
    car = creator.create()

    creator = TruckWorkShop()
    truck = creator.create()

    car.release()
    truck.release()