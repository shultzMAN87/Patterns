from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
import json
import xml.etree.ElementTree as ET



class AbstractSerializator(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def create_serializator_xml(self) -> AbstractSerializatorXML:
        pass

    @abstractmethod
    def create_serializator_json(self) -> AbstractSerializatorJSON:
        pass


class SerializatorForCSV(AbstractSerializator):
    def __init__(self, file_path):
        super().__init__(file_path)

    def create_serializator_xml(self) -> AbstractSerializatorXML:
        return SerializatorCSV4XML(self.file_path)

    def create_serializator_json(self) -> AbstractSerializatorJSON:
        return SerializatorCSV4JSON(self.file_path)


class SerializatorForXLS(AbstractSerializator):
    def __init__(self, file_path):
        super().__init__(file_path)

    def create_serializator_xml(self) -> AbstractSerializatorXML:
        return SerializatorXLS4XML(self.file_path)

    def create_serializator_json(self) -> AbstractSerializatorJSON:
        return SerializatorXLS4JSON(self.file_path)


class AbstractSerializatorXML(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def to_xml(self) -> str:
        pass

    @abstractmethod
    def from_xml(self) -> str:
        pass


class SerializatorCSV4XML(AbstractSerializatorXML):
    def __init__(self, file_path):
        super().__init__(file_path)

    def to_xml(self) -> str:
        csv_data = pd.read_csv(self.file_path)
        csv_data.columns = ['product', 'quantity']
        csv_data_list = csv_data.to_dict(orient='records')

        root = ET.Element("products")
        for product in csv_data_list:
            element = ET.Element("product")
            for key, val in product.items():
                child = ET.Element(key)
                child.text = str(val)
                element.append(child)

            root.append(element)

        xml_str = ET.tostring(root, encoding="utf-8", method="xml", xml_declaration=True)

        return xml_str.decode(encoding="utf-8")

    def from_xml(self) -> str:
        pass


class SerializatorXLS4XML(AbstractSerializatorXML):
    def __init__(self, file_path):
        super().__init__(file_path)

    def dict_to_xml(tag, d):
        element = ET.Element(tag)
        for key, val in d.items():
            child = ET.Element(key)
            child.text = str(val)
            element.append(child)
        return element

    def to_xml(self) -> str:
        xls_data = pd.read_excel(self.file_path, header=None)
        xls_data.columns = ['product', 'quantity']
        xls_data_list = xls_data.to_dict(orient='records')

        root = ET.Element("products")
        for product in xls_data_list:
            element = ET.Element("product")
            for key, val in product.items():
                child = ET.Element(key)
                child.text = str(val)
                element.append(child)

            root.append(element)

        xml_str = ET.tostring(root, encoding="utf-8", method="xml", xml_declaration=True)

        return xml_str.decode(encoding="utf-8")

    def from_xml(self) -> str:
        pass


class AbstractSerializatorJSON(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def to_json(self) -> str:
        pass

    @abstractmethod
    def from_json(self) -> str:
        pass


class SerializatorCSV4JSON(AbstractSerializatorJSON):
    def __init__(self, file_path):
        super().__init__(file_path)

    def to_json(self) -> str:
        csv_data = pd.read_csv(self.file_path)
        csv_data.columns = ['product', 'quantity']
        csv_data_dict = csv_data.to_dict(orient='records')

        return json.dumps(csv_data_dict, indent=4, ensure_ascii=False)

    def from_json(self) -> str:
        pass


class SerializatorXLS4JSON(AbstractSerializatorJSON):
    def __init__(self, file_path):
        super().__init__(file_path)

    def to_json(self) -> str:
        xls_data = pd.read_excel(self.file_path, header=None)
        xls_data.columns = ['product', 'quantity']
        xls_data_dict = xls_data.to_dict(orient='records')

        return json.dumps(xls_data_dict, indent=4, ensure_ascii=False)

    def from_json(self) -> str:
        pass


def client_code(serializ_factory: AbstractSerializator) -> None:
    serializ_json = serializ_factory.create_serializator_json()
    print(serializ_json.to_json())

    serializ_xml = serializ_factory.create_serializator_xml()
    print(serializ_xml.to_xml())


if __name__ == "__main__":
    client_code(SerializatorForXLS('./list_xls.xls'))

    client_code(SerializatorForCSV('./products.csv'))