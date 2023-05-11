import pandas
import finnhub
import xml.etree.ElementTree as xml
from enum import Enum

class xml_handler:
    class data_type(Enum):
        id = 0
        currency = 1
        description = 2
        displaySymbol = 3
        figi = 4
        isin = 5
        mic = 6
        shareClassFIGI = 7
        symbol = 8
        symbol2 = 9
        type = 10

    def get_indexer() -> int:
        xml_doc = xml.parse("store_values.xml")
        root_node = xml_doc.getroot()
        return int(root_node.find(".//indexer").text)

    def set_indexer(newIndex: int):
        xml_doc = xml.parse("store_values.xml")
        root_node = xml_doc.getroot()
        root_node.find(".//indexer").text = str(newIndex)

    def get_value(where_column: data_type) -> str:
        xml_doc = xml.parse("store_values.xml")
        root_node = xml_doc.getroot()

    def get_row(where_column: data_type) -> list[str]:
        xml_doc = xml.parse("store_values.xml")
        root_node = xml_doc.getroot()

    def insert_row(new_data: dict):
        xml_doc = xml.parse("store_values.xml")
        root_node = xml_doc.getroot()

        id: str = ""
        currency: str = ""
        description: str = ""
        display_symbol: str = ""
        figi: str = ""
        isin: str = ""
        mic: str = ""
        share_class_figi: str = ""
        symbol: str = ""
        symbol_2: str = ""
        type: str = ""

        values_node = root_node.find(".//values")
        id = str(xml_handler.get_indexer())
        for data in new_data.items():
            print(str(data))