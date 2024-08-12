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
    def set_os(self):
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

    def set_os(self):
        self.computer.os = "Windows 10"

    def get_computer(self) -> Computer:
        return self.computer


class ServerComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = "Xenon"

    def set_gpu(self):
        self.computer.gpu = "Intel"

    def set_ram(self):
        self.computer.ram = "128GB DDR5"

    def set_storage(self):
        self.computer.storage = "20TB HDD"

    def set_power_supply(self):
        self.computer.power_supply = "1500W Gold"

    def set_os(self):
        self.computer.os = "Linux"

    def get_computer(self) -> Computer:
        return self.computer


class Director:
    def __init__(self, builder_: ComputerBuilder):
        self._builder = builder_

    def build_gaming_computer(self):
        self._builder.set_cpu()
        self._builder.set_gpu()
        self._builder.set_ram()
        self._builder.set_storage()
        self._builder.set_power_supply()
        self._builder.set_os()

        return self._builder.get_computer()

    def build_server_computer(self):
        self._builder.set_cpu()
        self._builder.set_ram()
        self._builder.set_storage()
        self._builder.set_power_supply()
        self._builder.set_os()

        return self._builder.get_computer()


class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.power_supply = None
        self.os = None

    def __str__(self):
        return (f"Computer(cpu={self.cpu}, gpu={self.gpu},"
                f"ram={self.ram}, storage={self.storage}, power_supply={self.power_supply}, os={self.os})")


if __name__ == "__main__":
    # gaming_computer_builder = GamingComputerBuilder()
    # director = Director(gaming_computer_builder)
    # print(director.build_gaming_computer())

    server_computer_builder = ServerComputerBuilder()
    director = Director(server_computer_builder)
    print(director.build_server_computer())
    print(director.build_gaming_computer())
