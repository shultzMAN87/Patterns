from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd



class AbstractSerializator(ABC):
    @abstractmethod
    def create_serializator_xml(self) -> AbstractSerializatorXML:
        pass

    @abstractmethod
    def create_serializator_json(self) -> AbstractSerializatorJSON:
        pass


class SerializatorForCSV(AbstractSerializator):
    def create_serializator_xml(self) -> AbstractSerializatorXML:
        return SerializatorCSV4XML()

    def create_serializator_json(self) -> AbstractSerializatorJSON:
        return SerializatorCSV4JSON()


class SerializatorForXLS(AbstractSerializator):
    def create_serializator_xml(self) -> AbstractSerializatorXML:
        return SerializatorXLS4XML()

    def create_serializator_json(self) -> AbstractSerializatorJSON:
        return SerializatorXLS4JSON()


class AbstractSerializatorXML(ABC):
    @abstractmethod
    def to_xml(self, path_file: str) -> str:
        pass

    @abstractmethod
    def from_xml(self) -> str:
        pass


class SerializatorCSV4XML(AbstractSerializatorXML):
    def to_xml(self, path_file: str) -> str:
        return 'A'

    def from_xml(self) -> str:
        pass


class SerializatorXLS4XML(AbstractSerializatorXML):
    def to_xml(self, path_file: str) -> str:
        excel_data = pd.read_excel(path_file, header=None)
        data = pd.DataFrame(excel_data)
        return data

    def from_xml(self) -> str:
        pass


class AbstractSerializatorJSON(ABC):
    @abstractmethod
    def to_xml(self) -> str:
        pass

    @abstractmethod
    def from_xml(self) -> str:
        pass


class SerializatorCSV4JSON(AbstractSerializatorJSON):
    def to_xml(self) -> str:
        pass

    def from_xml(self) -> str:
        pass


class SerializatorXLS4JSON(AbstractSerializatorJSON):
    def to_xml(self) -> str:
        pass

    def from_xml(self) -> str:
        pass


def client_code(serializ_factory: AbstractSerializator) -> None:
    serializ_xml = serializ_factory.create_serializator_xml()
    print(serializ_xml.to_xml('./list_xls.xls'))


if __name__ == "__main__":
    client_code(SerializatorForXLS())