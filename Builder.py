from __future__ import annotations
from abc import ABC, abstractmethod


class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self):
        pass

    @abstractmethod
    def set_gpu(self):
        pass

    @abstractmethod
    def set_ram(self):
        pass

    @abstractmethod
    def set_storage(self):
        pass

    @abstractmethod
    def set_power_supply(self):
        pass

    @abstractmethod
    def get_computer(self) -> Computer:
        pass


class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = "Intel Core i9"

    def set_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"

    def set_ram(self):
        self.computer.ram = "32GB DDR5"

    def set_storage(self):
        self.computer.storage = "2TB SSD"

    def set_power_supply(self):
        self.computer.power_supply = "850W Gold"

    def get_computer(self) -> Computer:
        return self.computer


class Director:
    def __init__(self, builder: ComputerBuilder):
        self._builder = builder

    def build_computer(self):
        self._builder.set_cpu()
        self._builder.set_gpu()
        self._builder.set_ram()
        self._builder.set_storage()
        self._builder.set_power_supply()
        return self._builder.get_computer()


class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.power_supply = None

    def __str__(self):
        return f"Computer(cpu={self.cpu}, gpu={self.gpu}, ram={self.ram}, storage={self.storage}, power_supply={self.power_supply})"


if __name__ == "__main__":
    builder = GamingComputerBuilder()
    director = Director(builder)

    gaming_computer = director.build_computer()
    print(gaming_computer)

